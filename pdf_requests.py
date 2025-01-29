import requests
import pymupdf
import PyPDF2
from io import BytesIO
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from pdfminer.high_level import extract_text
from sentence_transformers import SentenceTransformer
import nltk
from nltk.tokenize import sent_tokenize
from gensim.models import Word2Vec


pdf_url = 'http://arxiv.org/pdf/cond-mat/0102536v1'
response = requests.get(pdf_url)

pdf_content = BytesIO(response.content)
pdf_text = extract_text(pdf_content)
pdf_text = pdf_text.replace("\n", " ").strip()
model = SentenceTransformer("all-MiniLM-L6-v2")
sentence = sent_tokenize(pdf_text)
print(sentence)
embeddings = model.encode(sentence)
print(embeddings.shape)

""" reader = PyPDF2.PdfReader(pdf_content)

text = ""
count = 0
for page in reader.pages:
    count += 1
    text += page.extract_text() """


#text = re.sub('\n', ' ', text).lower()
#print(re.sub('[^A-Za-z\\. -]','',text))
#vectorizer = TfidfVectorizer()
#embedding = vectorizer.fit_transform(text).toarray()

#text = re.sub(r'[^A-Za-z\\. - \\( \\)]+', '',text).lower().strip()
#print(re.sub('[\\.]','', text ))