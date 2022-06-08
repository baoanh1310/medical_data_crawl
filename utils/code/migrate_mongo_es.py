import uuid

from elasticsearch import helpers
from elasticsearch import Elasticsearch
import json
import pandas as pd
data_file = '../data/drugbank_clean.csv'

def createListJson(fn):
    data = []
    df = pd.read_csv(fn)
    df = df.fillna('')

    for idx, row in df.iterrows():
        # print(df.iloc[idx,:])
        new_df = {}
        new_df['drugId'] = df['id']
        new_df['drugName'] = df['tenThuoc']
        new_df['registerCode'] = df['soDangKy']
        new_df['drugPropertyNames'] = df['hoatChat']
        # new_df['drugProperties'] = df['taDuoc']
        new_df['category'] = df['phanLoai']
        new_df['country'] = df['nuocSx']
        # new_df['addressFrom'] = df['diaChiSx']
        # new_df['registerAddress'] = df['diaChiDk']
        new_df['registerCompany'] = df['congTyDk']
        new_df['price'] = df['giaKeKhai']
        new_df['expired'] = df['tuoiTho']
        new_df['standard'] = df['tieuChuan']
        new_df['drugType'] = df['nhomThuoc']
        # new_df['drugNum'] = df['soQuyetDinh']

        data.append(new_df)
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
        # print(item)
        yield item


if __name__ == '__main__':
    es_client = Elasticsearch([{'host': 'localhost', 'port': 9200}])

    # Take1:
    # Load all json data to lsit
    # Then yield

    try:
        response = helpers.bulk(es_client, bulk_json_data(data_file,
                                                          'drugs', '_doc'))
    except Exception as e:
        print('\nERROR: ', e)
