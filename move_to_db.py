from pymongo import MongoClient
from Create_embeddings import doc

client = MongoClient("mongodb://localhost:27017/")
db = client["Arxiv"]
collection = db["Arxiv Papers"]
collection.insert_many([doc])
#we need to bulk insert a list of dictionaries