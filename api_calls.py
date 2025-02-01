import feedparser
from api_funcs import *
from sentence_transformers import SentenceTransformer
import time
import tqdm

BASE_URL = 'http://export.arxiv.org/api/query?search_query=all:Machine%20Learning'
TOTAL_RESULTS = 300000
BATCH_SIZE = 1000
#Connect to client
client = MongoClient("mongodb://localhost:27017/")
db = client["Arxiv"]
collection = db["Arxiv Papers"]

#load in model
model = SentenceTransformer('all-MiniLM-L6-v2')
model = model.to('cuda')
""" meta_data = ['links','title', 'title_detail', 'id', 'guidislink','link','updated','updated_parsed','opensearch_totalresults','opensearch_startindex','opensearch_itemsperpage']
for meta in meta_data:
    print(data.feed[meta]) """

#initialize potential searches
fields = [
    "Algebraic%20Geometry", "Algebraic%20Topology", "Analysis%20of%20PDEs", "Category%20Theory",
    "Classical%20Analysis%20and%20ODEs", "Combinatorics", "Commutative%20Algebra", "Complex%20Variables",
    "Differential%20Geometry", "Dynamical%20Systems", "Functional%20Analysis", "General%20Mathematics",
    "General%20Topology", "Geometric%20Topology", "Group%20Theory", "History%20and%20Overview",
    "Information%20Theory", "K-Theory%20and%20Homology", "Logic", "Mathematical%20Physics",
    "Metric%20Geometry", "Number%20Theory", "Numerical%20Analysis", "Operator%20Algebras",
    "Optimization%20and%20Control", "Probability", "Quantum%20Algebra", "Representation%20Theory",
    "Rings%20and%20Algebras", "Spectral%20Theory", "Statistics%20Theory", "Symplectic%20Geometry"
]

BASE_URL_1 = 'http://export.arxiv.org/api/query?search_query=all:'

'''
Retrieve batch of articles, retrieve embeddings for db,
push to db in dictionary format.
'''
for start in tqdm.tqdm(range(0, TOTAL_RESULTS, BATCH_SIZE)):
    url = BASE_URL + f'&start={start}&max_results={BATCH_SIZE}'
    data = feedparser.parse(url)
    entry_data = ['arxiv_doi', 'title', 'summary','authors']
    arr_docs = []

    for data in data.entries:
        if article_in_mongodb(data['arxiv_doi'], collection):
                print('entered continue')
                continue
        doc = entry_metadata(data, entry_data)
        summary_embeddings(doc, model)
        title_embeddings(doc, model)
        arr_docs.append(doc)
    if arr_docs:
        push_to_db(arr_docs, collection)
    
    time.sleep(3)

if __name__ == '__main__':
    pass

""" index = find_index(data, 0)
pdf_url = data.entries[0].links[index].href
pdf = requests.get(pdf_url) """
