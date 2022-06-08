from pymongo import MongoClient
import bson
import pandas as pd
# import pytz
from datetime import datetime
from elasticsearch import helpers
from elasticsearch import Elasticsearch
import json
import uuid
from tqdm import tqdm

def createListJson(fn):
    data = []
    df = pd.read_csv(fn)
    df = df.fillna('')
    df.drop(['Unnamed: 0'], axis=1, inplace=True)

    for idx, row in df.iterrows():
        data.append(row)
    return data

def bulk_json_data(data_file, index, doc_type):
    json_list = createListJson(data_file)

    for doc in json_list:
        item = {
            "_index": index,
            "_type": doc_type,
            "_id":  uuid.uuid4(),
            "_source": doc
        }
        yield item


if __name__ == '__main__':
    MONGODB_URI = "mongodb://baoanh:baoanh@localhost:27017"
    MONGODB_DATABASE = 'vaipeapis'
    CRAWLER_COLLECTION = "drugs"

    connection = MongoClient(MONGODB_URI)
    db = connection[MONGODB_DATABASE]
    collection = db.database[CRAWLER_COLLECTION]

    # print(collection.name)
    # get list data
    
    drugs = []
    cursor = collection.find()

    # print(cursor)
    for drug in cursor:
        drug['_id'] = str(drug['_id'])
        drugs.append(drug)
    df = pd.DataFrame(drugs)
    # print(df.columns)
    
    df['drugId'] = df['_id']
    df.drop(['_id'], axis=1, inplace=True)

    df.to_csv('drug_es.csv')
    
    # convert dataframe to json format
    with open('drugs.json', 'w') as f:
        for idx, row in tqdm(df.iterrows()):
            str_idx = str(idx+1)
            idx_line = {"index": {"_index" : "drugs", "_id": str_idx}}
            f.write(json.dumps(idx_line))    
            f.write('\n')
            f.write(json.dumps(row.to_dict()))
            # f.write(json.dumps(row))
            f.write('\n')


