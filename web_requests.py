import requests
import pymupdf
import PyPDF2
from io import BytesIO

pdf_url = 'http://arxiv.org/pdf/cond-mat/0102536v1'
response = requests.get(pdf_url)

pdf_content = BytesIO(response.content)
reader = PyPDF2.PdfReader(pdf_content)
text = ""
for page in reader.pages:
    text += page.extract_text()

print(text)