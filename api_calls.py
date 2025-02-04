import feedparser
from api_funcs import *
from sentence_transformers import SentenceTransformer
import time
import tqdm




#Connect to client
#client = MongoClient("mongodb://localhost:27017/")


#load in model


#initialize potential searches
fields = [
    #"Algebraic%20Geometry", "Algebraic%20Topology", "Analysis%20of%20PDEs", "Category%20Theory",
    #"Classical%20Analysis%20and%20ODEs", "Combinatorics", "Commutative%20Algebra", "Complex%20Variables",
    #"Differential%20Geometry", "Dynamical%20Systems", "Functional%20Analysis", "General%20Mathematics",
    #"General%20Topology", "Geometric%20Topology", "Group%20Theory", "History%20and%20Overview",
    "Information%20Theory", "K-Theory%20and%20Homology", "Logic", "Mathematical%20Physics",
    "Metric%20Geometry", "Number%20Theory", "Numerical%20Analysis", "Operator%20Algebras",
    "Optimization%20and%20Control", "Probability", "Quantum%20Algebra", "Representation%20Theory",
    "Rings%20and%20Algebras", "Spectral%20Theory", "Statistics%20Theory", "Symplectic%20Geometry"
]
#up to beggining of category theory
'''
Retrieve batch of articles, retrieve embeddings for db,
push to db in dictionary format.
'''
""" url = BASE_URL + f'&start={0}&max_results={1}'
data = feedparser.parse(url)
total = data.feed["opensearch_totalresults"] """

class API():
    def __init__(self):
        self.BASE_URL = 'http://export.arxiv.org/api/query?search_query=all:'
        self.TOTAL_RESULTS = 300000
        self.BATCH_SIZE = 2000

    def connect_db(self):
        client = MongoClient("mongodb://localhost:27017/")
        db = client["Arxiv"]
        self.collection = db["Arxiv Papers"]
    
    def load_model(self):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.model = self.model.to('cuda')

    def data_retrieval(self):
        for field in fields:
            for start in tqdm.tqdm(range(0, self.TOTAL_RESULTS, self.BATCH_SIZE)):
                url = self.BASE_URL + field + f'&start={start}&max_results={self.BATCH_SIZE}'
                data = feedparser.parse(url)
                index = 0
                while not data.entries and index != 10:
                    time.sleep(5)
                    index += 1
                    print("Finding data")
                    url = self.BASE_URL + field + f'&start={start}&max_results={self.BATCH_SIZE}'
                    data = feedparser.parse(url)
                if index == 10 and not data.entries:
                    break
                entry_data = ['arxiv_doi', 'title', 'summary','authors']
                arr_docs = []
                continued = 0
                for data in data.entries:
                    if continued == 20:
                        break
                    if 'arxiv_doi' in data and article_in_mongodb(data['arxiv_doi'], self.collection):
                            continued += 1
                            print(data['arxiv_doi'])
                            print('entered continue')
                            continue
                    if 'title' in data and title_in_mongod(data['title'], self.collection):
                        print('entered title')
                        continue
                    doc = entry_metadata(data, entry_data)
                    #summary_embeddings(doc, self.model)
                    #title_embeddings(doc, self.model)
                    arr_docs.append(doc)
                if arr_docs:
                    print("pushing")
                    push_to_db(arr_docs, self.collection)
                else:
                    print(start)
                    print(data.entries)
                    break
                remove_duplicates()

                time.sleep(5)

if __name__ == '__main__':
    inst = API()
    inst.connect_db()
    inst.load_model()
    inst.data_retrieval()