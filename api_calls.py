import urllib, urllib.request
import requests
import feedparser
import pandas as pd
from api_funcs import *
import re
from sentence_transformers import SentenceTransformer


url = 'http://export.arxiv.org/api/query?search_query=all:electron&start=0&max_results=1'
data = feedparser.parse(url)

""" meta_data = ['links','title', 'title_detail', 'id', 'guidislink','link','updated','updated_parsed','opensearch_totalresults','opensearch_startindex','opensearch_itemsperpage']
for meta in meta_data:
    print(data.feed[meta]) """

entry_data = ['arxiv_doi', 'title','published','updated','summary','authors', 'arxiv_affiliation']
doc = entry_metadata(data, entry_data)







if __name__ == '__main__':
    pass



""" index = find_index(data, 0)
pdf_url = data.entries[0].links[index].href
pdf = requests.get(pdf_url) """
