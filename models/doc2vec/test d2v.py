from gensim.models.doc2vec import Doc2Vec
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet
from nltk import pos_tag
import string
from nltk.stem import WordNetLemmatizer
import numpy as np
import re

lemmatizer = WordNetLemmatizer()

def get_wordnet_pos(treebank_tag):
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
    
def preprocessing(summaries):
    summaries[0] = summaries[0].lower()
    summaries[0] = summaries[0].translate(str.maketrans("", "", string.punctuation))
    tokens = word_tokenize(summaries[0])
    pos_tags = pos_tag(tokens)
    lemmatized_tokens = [
        lemmatizer.lemmatize(word, get_wordnet_pos(pos))
        for word, pos in pos_tags
    ]
    return [" ".join(lemmatized_tokens)]

model = Doc2Vec.load("d2v.model")
user_input = "vector"
user_input = preprocessing([user_input])
test_data = word_tokenize(user_input[0])
v1 = model.infer_vector(test_data, epochs = 50)

print("complex" in model.wv.key_to_index)
print("number" in model.wv.key_to_index)

similar_docs = model.docvecs.most_similar([v1], topn = 5)

summary = np.load('summary.npy')
""" print(summary[4661])
temp = []
for num in summary:
    found = re.search("withdraw", num[0])
    temp.append(found is None)
summary = summary[temp]
print(summary[4661])
 """

for doc_id, similarity in similar_docs:
    print(doc_id)
    print(f"Document ID: {doc_id}, Similarity: {similarity}")
    print(f"Summary: {summary[int(doc_id)]}\n")