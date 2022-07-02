from datetime import datetime
from flask import Flask, jsonify, request
from elasticsearch import Elasticsearch

es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def hello():
    return "Hello"

@app.route('/', methods=['GET'])
def index():
    results = es.get(index='drugs', doc_type='_doc', id='1')
    return jsonify(results['_source'])


@app.route('/suggest', methods=['GET'])
def suggest_drug_with_name(size_query=100):
    args = request.args
    name = args.get('name')
    value = "{}.*".format(name)
    query = {
        "query": {
            "match_phrase_prefix": {
                "drugName": {
                    "query": "{}.".format(name)
                }
            }
        }
    }

    # match_docs = es.search(body=query, index="drugs", doc_type='_doc')
    match_docs = es.search(body=query, index="drugs")
    if match_docs['hits']['total']['value'] > 0:
        docs = [doc['_source'] for doc in match_docs['hits']['hits']]
        docs = [{ "drugId": doc["drugId"], "drugName": doc["drugName"] } for doc in docs]
        
        res = {
            "appStatus": 200,
            "data": {
                "result": {
                    "values": docs 
                }
            }
        }
        return res

    return {
            "appStatus": 200,
            "data": {
                "result": {
                    "values": [] 
                }
            }
        }

@app.route('/search', methods=['GET'])
def search_drug_with_name(size_query=100):
    args = request.args
    name = args.get('name')
    # query = {"size": size_query, "query": {"match": {"drugName": '{}.*'.format(name)}}}
    query = {
        "query": {
            "bool": {
                "must": [
                    {
                        "match_phrase_prefix": {
                            "drugName": {
                                "query": "{}.".format(name)
                            }
                        }
                    }
                ],
                "filter": [],
                "should": [],
                "must_not": []
            }
        },
        "aggs": {
            "auto_complete": {
                "terms": {
                    "field": "name.keyword",
                    "order": {
                        "_count": "desc"
                    },
                    "size": 8
                }
            }
        }
    }
    # match_docs = es.search(body=query, index="drugs", doc_type='_doc')
    match_docs = es.search(body=query, index="drugs")
    if match_docs['hits']['total']['value'] > 0:
        docs = [doc['_source'] for doc in match_docs['hits']['hits']]
        # docs = [{ "drugId": doc["drugId"], "drugName": doc["drugName"] } for doc in docs]
        
        res = {
            "appStatus": 200,
            "data": {
                "result": {
                    "values": docs 
                }
            }
        }
        return res

    return {
            "appStatus": 200,
            "data": {
                "result": {
                    "values": [] 
                }
            }
        }

app.run(host='0.0.0.0', port=5757, debug=True)
