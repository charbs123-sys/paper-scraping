from api_calls import doc
from gensim.models import Word2Vec
#from nltk.tokenize import word_tokenize
from sentence_transformers import SentenceTransformer

#sentence embeddings
text_summary = doc['summary'].split(".")
model = SentenceTransformer('all-MiniLM-L6-v2')
embedding = model.encode(text_summary)
doc['summary_embedded'] = embedding.tolist()

text_title = doc['title']
embedding_title = model.encode(text_title)
doc['title_embedded'] = embedding_title.tolist()

