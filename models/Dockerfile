FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt requirements.txt
COPY complete_tfidf.py complete_tfidf.py
COPY tfidf_vectorized.pkl tfidf_vectorized.pkl
COPY tfidf.pkl tfidf.pkl
COPY original.npy original.npy


RUN pip install -r requirements.txt

CMD ["python", "complete_tfidf.py"]