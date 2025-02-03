from pymongo import MongoClient
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import pickle
import os
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize
import string
from nltk import pos_tag
from nltk.stem import WordNetLemmatizer
import copy
from sklearn.feature_extraction.text import TfidfVectorizer

class Model():
    def __init__(self):
        vectorizer = 'tfidf_vectorized.pkl'
        tfidf_model = 'tfidf.pkl'
        self.original_summary = np.load('original.npy')
        self.summary = np.load("summary.npy")
        self.lemmatizer = WordNetLemmatizer()
        self.summary_full = [self.summary[index][0] for index in range(len(self.summary))]

        if os.path.exists(vectorizer) and os.path.exists(tfidf_model):
            with open(vectorizer, "rb") as f:
                self.tfidf_vectorizer = pickle.load(f)
            with open(tfidf_model, "rb") as f:
                self.tfidf_mat = pickle.load(f)
        else:
            print("Model needs to be trained")

    def train(self):
        if os.path.exists("summary.npy"):
            print("This model has already been trained")
            return None
        
        client = MongoClient("mongodb://localhost:27017/")
        db = client["Arxiv"]
        collection = db["Arxiv Papers"]
        
        summary = [[doc["summary"]] for doc in collection.find()]
        original_summary = copy.deepcopy(summary)
        np.save("original.npy", original_summary)
        
        for i in range(len(summary)):
            summary[i] = self.preprocessing(summary[i])
        
        np.save("summary.npy", summary)

        vectorizer = 'tfidf_vectorized.pkl'
        tfidf_model = 'tfidf.pkl'

        tfidf_vectorizer = TfidfVectorizer(lowercase=True, stop_words='english')
        tfidf_mat = tfidf_vectorizer.fit_transform(self.summary_full)
        with open(vectorizer, "wb") as f:
            pickle.dump(tfidf_vectorizer, f)
        with open(tfidf_model, "wb") as f:
            pickle.dump(tfidf_mat, f)
        print("saved to cache")

    def get_wordnet_pos(self, treebank_tag):
        if treebank_tag.startswith('J'):
            return wordnet.ADJ
        elif treebank_tag.startswith('V'):
            return wordnet.VERB
        elif treebank_tag.startswith('N'):
            return wordnet.NOUN
        elif treebank_tag.startswith('R'):
            return wordnet.ADV
        else:
            return wordnet.NOUN  # Default to noun
        
    def preprocessing(self, summaries):
        summaries[0] = summaries[0].lower()
        summaries[0] = summaries[0].translate(str.maketrans("", "", string.punctuation))
        tokens = word_tokenize(summaries[0])
        pos_tags = pos_tag(tokens)
        lemmatized_tokens = [
            self.lemmatizer.lemmatize(word, self.get_wordnet_pos(pos))
            for word, pos in pos_tags
        ]
        return [" ".join(lemmatized_tokens)]

        
    def predict(self, user_input):
        user_input = self.preprocessing(user_input)
        new_tfidf = self.tfidf_vectorizer.transform(user_input)

        similarities = cosine_similarity(new_tfidf, self.tfidf_mat)

        similarities_np = np.array(similarities[0])

        highest = np.argpartition(similarities_np, -5)[-5:]

        clean_arr = np.array([[high, similarities_np[high]] for high in highest])
        clean_arr = clean_arr[clean_arr[:,1].argsort()][::-1]

        client = MongoClient("mongodb://localhost:27017/")
        db = client["Arxiv"]
        collection = db["Arxiv Papers"]

        summary_top_5 = np.array(self.original_summary)[highest]

        for summarized in summary_top_5:
            query = {"summary" : summarized[0]}
            found = collection.find(query)
            for document in found:
                print(document['title'], "\n")



if __name__ == "__main__":
    model = Model()
    model.predict(["machine!!"])