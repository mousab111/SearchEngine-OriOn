from flask import Flask, render_template, request
from elasticsearch import Elasticsearch
from Services.SearchService.SearchEngine import SearchEngine
from flask import Flask, jsonify, request
from Services.FilesManagmentService.FilesServices import *


app = Flask(__name__)


es = Elasticsearch(['http://127.0.0.1:5000'])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    query = request.form.get('query')
    dataset_type = request.form.get('dataset_type')
    
    searchEngine = SearchEngine("trec-tot-2023-train")
    search_results = searchEngine.search(query)
    print(searchEngine.results)


    # Formater les résultats de recherche
    results = []
    for doc in search_results:
        result = { 
            'doc_id': doc.page_title ,
            'content': doc.text 
        }    
        results.append(result)
    return render_template('results.html', results=results, query=query)

    

@app.route("/suggestions", methods=["GET"])
def get_suggestions():
    query = request.args.get("query")
    #dataset_type = request.args.get('dataset_type')
    dataset_type = "trec-tot-2023-train"
    suggestions = generate_suggestions( dataset_type , query)
    return jsonify(suggestions)

def generate_suggestions( dataset_type , query):
    suggestions = getDatasetFileContentAsArray(  dataset_type ,"suggestions.txt")
       
    return suggestions

if __name__ == '__main__':
    app.run(debug=True)
    59 
    
    
    
    
    
    
    
    