import uuid

from elasticsearch import helpers
from elasticsearch import Elasticsearch
import json
import pandas as pd
data_file = '../data/drug_clean.csv'

def createListJson(fn):
    data = []
    df = pd.read_csv(fn)
    df = df.fillna('')

    for idx, row in df.iterrows():
        # print(df.iloc[idx,:])
        obj = {}
        obj['soDangKy'] = row['soDangKy']
        obj['tenThuoc'] = row['tenThuoc']
        obj['tenThuocDenoised'] = row['denoisedTenThuoc']
        obj['nhomThuoc'] = row['nhom-thuoc']
        obj['baoChe'] = row['baoChe']
        obj['cachDung'] = row['cach-dung']
        # obj['cuTheCacThanhPhan'] = row['cu-the-cac-thanh-phan']
        obj['chiDinh'] = row['chi-dinh']
        obj['chongChiDinh'] = row['chong-chi-dinh']
        obj['congTySx'] = row['congTySx']
        obj['congTySxCode'] = row['congTySxCode']
        obj['dangBaoChe'] = row['baoChe']
        obj['dongGoi'] = row['dongGoi']
        obj['hoatChat'] = row['hoatChat']
        obj['nongDo'] = row['nongDo']
        obj['thanhPhan'] = row['thanh-phan']
        obj['giaKeKhai'] = row['giaKeKhai']
        obj['tacDungPhu'] = row['tac-dung-phu']
        obj['dePhong'] = row['de-phong']
        obj['tuoiTho'] = row['tuoiTho']
        obj['tuongTacThuoc'] = row['tuong-tac-thuoc']
        obj['nuocDk'] = row['nuocDk']
        obj['nuocSx'] = row['nuocSx']

        data.append(obj)
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
        print(item)
        yield item


if __name__ == '__main__':
    es_client = Elasticsearch([{'host': '202.191.57.62', 'port': 9200}])

    # Take1:
    # Load all json data to lsit
    # Then yield

    try:
        response = helpers.bulk(es_client, bulk_json_data(data_file,
                                                          'emed', '_doc'))
    except Exception as e:
        print('\nERROR: ', e)
