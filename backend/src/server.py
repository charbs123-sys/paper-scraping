from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
from models.complete_tfidf import Model 
from models.complete_d2v import Model as Model2

app = Flask(__name__)
CORS(app)

client = MongoClient("mongodb://localhost:27017")
db = client["Arxiv"]
collection = db["Arxiv Papers"]

model = Model()
model2 = Model2()

# Add server routes for functions
@app.get('/recommendations')
def recommend_papers():
    user_query = request.args.get('query')
    model_option = request.args.get('model')
    dm_option = request.args.get('option')
    
    if not user_query:
        return jsonify({'error': 'Query parameter is required'}), 400
    print([user_query])
    print(model_option)
    print(dm_option)
    
    if model_option == 'model1':
        recommendations = model.predict([user_query])
        return jsonify({'results' : recommendations})
    elif model_option == 'model2':
        recommendations = model2.test(user_query, dm_option)
        return jsonify({'results' : recommendations})


if __name__ == '__main__':
    model.train()
    model2.train()
    model2.train(dm=1)
    app.run(port=5000, debug=True, host='0.0.0.0')
    
