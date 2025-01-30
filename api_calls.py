import urllib, urllib.request
import requests
import feedparser
import pandas as pd
from api_funcs import *
import re
from sentence_transformers import SentenceTransformer
from tokenizers import Tokenizer
import time
import tqdm
import asyncio
import aiohttp

BASE_URL = 'http://export.arxiv.org/api/query?search_query=all:Machine%20Learning'
TOTAL_RESULTS = 300000
BATCH_SIZE = 1000
#Connect to client
client = MongoClient("mongodb://localhost:27017/")
db = client["Arxiv"]
collection = db["Arxiv Papers"]
model = SentenceTransformer('all-MiniLM-L6-v2')
model = model.to('cuda')
""" meta_data = ['links','title', 'title_detail', 'id', 'guidislink','link','updated','updated_parsed','opensearch_totalresults','opensearch_startindex','opensearch_itemsperpage']
for meta in meta_data:
    print(data.feed[meta]) """

for start in tqdm.tqdm(range(0, TOTAL_RESULTS, BATCH_SIZE)):
    url = BASE_URL + f'&start={start}&max_results={BATCH_SIZE}'
    data = feedparser.parse(url)
    entry_data = ['arxiv_doi', 'title', 'summary','authors']
    arr_docs = []

    for data in data.entries:
        #if 'arxiv_doi' not in data or article_in_mongodb(data['arxiv_doi'], collection):
        #        print('entered continue')
        #        continue
        doc = entry_metadata(data, entry_data)
        summary_embeddings(doc, model)
        title_embeddings(doc, model)
        arr_docs.append(doc)
    if arr_docs:
        push_to_db(arr_docs, collection)
    
    time.sleep(3)

#asynchronous runs
""" async def batch_url(session, start):
    url = BASE_URL + f'&start={start}&max_results={BATCH_SIZE}'
    async with session.get(url) as response:
        if response.status == 200:
            data = await response.text()
            return feedparser.parse(data)
        else:
            print("failed batch fetching")
            return None

async def processing_inserting_batch(session, start):
    data = await batch_url(session, start)
    if not data:
        return

    entry_data = ['arxiv_doi', 'title', 'summary', 'authors']
    arr_docs = []

    for entry in data.entries:
        if 'arxiv_doi' in entry: 
            if article_in_mongodb(entry['arxiv_doi'], collection):
                continue
        doc = entry_metadata(entry, entry_data)
        summary_embeddings(doc, model)
        title_embeddings(doc, model)
        arr_docs.append(doc)

    if arr_docs:
        push_to_db(arr_docs, collection)

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = []
        for start in tqdm.tqdm(range(0, TOTAL_RESULTS, BATCH_SIZE)):
            tasks.append(processing_inserting_batch(session, start))
            if len(tasks) >= CONCURRENT_REQUESTS:
                await asyncio.gather(*tasks)
                tasks = []
                time.sleep(3)  # Respect arXiv API rate limits
        if tasks:
            await asyncio.gather(*tasks)

asyncio.run(main()) """


""" doc = entry_metadata(data.entries[0], entry_data)
tokenizer = Tokenizer.from_pretrained('bert-base-cased')
encoded = tokenizer.encode(doc['summary'])
print(encoded.tokens) """
if __name__ == '__main__':
    pass



""" index = find_index(data, 0)
pdf_url = data.entries[0].links[index].href
pdf = requests.get(pdf_url) """
