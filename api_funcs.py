import re
from sentence_transformers import SentenceTransformer
from pymongo import MongoClient
import random

def find_index(data, index):
    #Finding index containing file pdf
    while True:
        if 'title' not in data.entries[0].links[index].keys():
            index += 1
            continue
        if data.entries[0].links[index].title != 'pdf':
            index += 1
        else:
            return index
        return -1


def entry_metadata (data, entry_data):
    '''
    Creating dictionary for relevant metadata
    to be imported into a mongodb database
    '''
    base = data
    
    if entry_data[0] not in base:
        doi = None
    else:
        doi = base[entry_data[0]]
    
    if entry_data[1] not in base:
        title = None
    else:
        title = base[entry_data[1]].lower()

    if entry_data[2] not in base:
        summary = None
    else:
        summary = base[entry_data[2]].lower()
        summary = re.sub("\n", " ", summary)

    if entry_data[3] not in base:
        authors = None
    else:
        authors = base[entry_data[3]]  # to normalize later
        authors = [nam.name.lower() for nam in authors]

    """     title = base[entry_data[index]].lower()
    index += 1
    summary = base[entry_data[index]].lower()
    summary = re.sub("\n"," ", summary)
    index += 1
    authors = base[entry_data[index]] #to normalize later
    authors = [nam.name.lower() for nam in authors] """

    mong = {
        "doi" : doi,
        "title" : title,
        "summary" : summary,
        "authors" : authors,
    }
    return mong


#sentence embeddings
def summary_embeddings(doc, model):
    text_summary = doc['summary'].split(".")
    embedding = model.encode(text_summary)
    doc['summary_embedded'] = embedding.tolist()

def title_embeddings(doc, model):
    text_title = doc['title']
    embedding_title = model.encode(text_title)
    doc['title_embedded'] = embedding_title.tolist()


def article_in_mongodb(doi, collection):
    article = collection.find_one({'doi':doi})
    return article is not None

def title_in_mongod (title, collection):
    article = collection.find_one({'title': title})
    return article is not None

def push_to_db(doc, collection):
    collection.insert_many(doc)

def remove_duplicates():
    client = MongoClient("mongodb://localhost:27017/")
    db = client["Arxiv"]
    collection = db["Arxiv Papers"]

    pipeline = [
        {
            "$group": {
                "_id": "$title",  # Group by the title field
                "ids": { "$push": "$_id" },  # Collect all document IDs for each title
                "count": { "$sum": 1 }  # Count the number of occurrences
            }
        },
        {
            "$match": {
                "count": { "$gt": 1 }  # Filter titles that appear more than once
            }
        }
    ]

    duplicates = collection.aggregate(pipeline)

    for duplicate in duplicates:
        title = duplicate["_id"]
        ids = duplicate["ids"]  # List of document IDs for this title
        # Keep the first document and delete the rest
        keep_id = ids[0]  # Keep the first occurrence
        delete_ids = ids[1:]  # IDs to delete
        # Delete duplicate documents
        if delete_ids:
            collection.delete_many({"_id": {"$in": delete_ids}})
            print(f"Removed {len(delete_ids)} duplicates for title: {title}")

    print("Duplicate removal complete!")