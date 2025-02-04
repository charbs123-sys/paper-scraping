from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
from models.tfidf_samples.complete_tfidf import Model

app = Flask(__name__)
CORS(app)

client = MongoClient("mongodb://localhost:27017")
db = client["Arxiv"]
collection = db["Arxiv Papers"]

model = Model()

# Add server routes for functions
@app.get('/recommendations')
def recommend_papers():
    user_input = request.args.get('query')
    if not user_input:
        return jsonify({'error': 'Query parameter is required'}), 400
    print([user_input])
    recommendations = model.predict([user_input])
    return jsonify({'results' : recommendations})


if __name__ == '__main__':
    model.train()
    app.run(port=5000, debug=True, host='0.0.0.0')
    
