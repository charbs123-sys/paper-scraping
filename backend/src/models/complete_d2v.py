from pymongo import MongoClient
from nltk.tokenize import word_tokenize
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
import numpy as np
from gensim.models.doc2vec import Doc2Vec
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet
from nltk import pos_tag
import string
from nltk.stem import WordNetLemmatizer
import re
import os

class Model():
    def __init__(self):
        if not os.path.exists("summary.npy"):
            print("summary needs to be generated")
            self.generate_summary()
        else:
            print("summary already generated")
        
        self.summary = np.load('summary.npy')

        self.summary_full = [self.summary[index][0] for index in range(len(self.summary))]
        self.summary_full = self.summary_full[0:10000] #slicing for now to decrease computation time
        self.tagged_data = [TaggedDocument(words = word_tokenize(_d.lower()), tags = [str(i)]) for i, _d in enumerate(self.summary_full)]
        self.lemmatizer = WordNetLemmatizer()

        self.original_summary = np.load("original.npy")

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
    
    def generate_summary(self):
        client = MongoClient("mongodb://localhost:27017/")
        db = client["Arxiv"]
        collection = db["Arxiv Papers"]
        self.summary = [[doc["summary"]] for doc in collection.find()]
        
        print("Creating summary")
        for i in range(len(self.summary)):
            self.summary[i] = self.preprocessing(self.summary[i])

        np.save("summary.npy", self.summary)

    def train(self, vec_size = 200, alpha = 0.025, min_alpha = 0.00025, min_count = 1, max_epochs = 100, dm = 0):
        if dm == 0 and os.path.exists("d2v0.model"):
            print("Model dm = 0 already trained")
            return None
        elif dm == 1 and os.path.exists("d2v1.model"):
            print("Model dm = 1 already trained")
            return None
        else:
            print("Training models")
        
        self.model = Doc2Vec(vector_size = vec_size, alpha = alpha, min_alpha = min_alpha, min_count = min_count, dm = dm, epochs = max_epochs)
        self.model.build_vocab(self.tagged_data)
        self.model.train(self.tagged_data, total_examples = self.model.corpus_count, epochs = 100)
        
        if dm == 0:
            self.model.save("d2v0.model")
        else:
            self.model.save("d2v1.model")

        print("Model Saved")
    
    def test(self, user_input, dm):
        
        client = MongoClient("mongodb://localhost:27017/")
        db = client["Arxiv"]
        collection = db["Arxiv Papers"]

        if dm == 0:
            model = Doc2Vec.load("d2v0.model")
        else:
            model = Doc2Vec.load("d2v1.model")
        
        user_input = self.preprocessing([user_input])
        test_data = word_tokenize(user_input[0])

        v1 = model.infer_vector(test_data, epochs = 50)
        similar_docs = model.docvecs.most_similar([v1], topn = 5)
        results = []

        for doc_id, similarity in similar_docs:
            query = {"summary" : self.original_summary[int(doc_id)][0]}
            found = collection.find(query)
            for document in found:
              results.append({
                    'title': document['title'],
                    'summary': document['summary']
                })

        return results 
            


# D2V = Model()
# D2V.train()
# D2V.test("Algebraic Geometry")