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

def push_to_db(doc, collection):
    collection.insert_many(doc)