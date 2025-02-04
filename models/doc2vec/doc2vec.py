from pymongo import MongoClient
from nltk.tokenize import word_tokenize
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
import numpy as np

summary = np.load('summary.npy')



summary_full = [summary[index][0] for index in range(len(summary))]
summary_full = summary_full[0:10000]
tagged_data = [TaggedDocument(words = word_tokenize(_d.lower()), tags = [str(i)]) for i, _d in enumerate(summary_full)]

vec_size = 200
alpha = 0.025
min_alpha = 0.00025
min_count = 1
max_epochs = 100

model = Doc2Vec(vector_size = 200, alpha = alpha, min_alpha = 0.00025, min_count = 2, dm = 0, epochs = 50)
model.build_vocab(tagged_data)

model.train(tagged_data, total_examples = model.corpus_count, epochs = 100)




model.save("d2v.model")
print("saving model")