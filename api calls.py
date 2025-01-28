import urllib, urllib.request
import requests
import feedparser
import pandas as pd
from api_funcs import *


url = 'http://export.arxiv.org/api/query?search_query=all:electron&start=0&max_results=1'
data = feedparser.parse(url)

meta_data = ['links','title', 'title_detail', 'id', 'guidislink','link','updated','updated_parsed','opensearch_totalresults','opensearch_startindex','opensearch_itemsperpage']
#for meta in meta_data:
#    print(data.feed[meta])

entry_data = ['title','id','published','updated','summary','author','authors','updated', 'link', 'arxiv_affiliation','arxiv_doi','links','tags']
#for entry in entry_data:
#    print(data.entries[0][entry])


index = find_index(data, 0)
pdf_url = data.entries[0].links[index].href

pdf = requests.get(pdf_url)
print(pdf)