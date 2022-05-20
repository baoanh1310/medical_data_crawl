import requests
import json
import pandas as pd


if __name__=="__main__":
    lst_item = []
    item_per_page = 20
    for i in range(1, 51):

        r = requests.get(r'https://drugbank.vn/services/drugbank/api/public/thuoc?page={0}&size={1}&isHide=Yes&sort=tenThuoc,asc&sort=id'.format(i, item_per_page))
        item_json_lst = json.loads(r.text)

        for item_json in item_json_lst:
            item = {}
            item['id'] = item_json['id']
            item['tenThuoc'] = item_json['tenThuoc']
            item['soQuyetDinh'] = item_json['soQuyetDinh']
            item['soDangKy'] = item_json['soDangKy']
            item['hoatChat'] = item_json['hoatChat']
            item['phanLoai'] = item_json['phanLoai']
            item['nongDo'] = item_json['nongDo']
            item['taDuoc'] = item_json['taDuoc']
            item['baoChe'] = item_json['baoChe']
            item['dongGoi'] = item_json['dongGoi']
            item['tieuChuan'] = item_json['tieuChuan']
            item['tuoiTho'] = item_json['tuoiTho']
            item['congTySx'] = item_json['congTySx']
            item['congTySxCode'] = item_json['congTySxCode']
            item['nuocSx'] = item_json['nuocSx']
            item['diaChiSx'] = item_json['diaChiSx']
            item['congTyDk'] = item_json['congTyDk']
            item['nuocDk'] = item_json['nuocDk']
            item['diaChiDk'] = item_json['diaChiDk']
            item['giaKeKhai'] = item_json['giaKeKhai']
            item['nhomThuoc'] = item_json['nhomThuoc']
            lst_item.append(item)

    df = pd.DataFrame(data=lst_item)
    df.to_csv('../../utils/data/drugbankvn.csv')