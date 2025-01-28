import requests
import pymupdf
import PyPDF2
from io import BytesIO
import re
from sklearn.feature_extraction.text import TfidfVectorizer

pdf_url = 'http://arxiv.org/pdf/cond-mat/0102536v1'
response = requests.get(pdf_url)

pdf_content = BytesIO(response.content)
reader = PyPDF2.PdfReader(pdf_content)

text = ""
count = 0
for page in reader.pages:
    count += 1
    text += page.extract_text()

print(text)

#vectorizer = TfidfVectorizer()
#embedding = vectorizer.fit_transform(text).toarray()

#print(re.sub(r'[^A-Za-z0-9 ]+', '',text).lower().strip())