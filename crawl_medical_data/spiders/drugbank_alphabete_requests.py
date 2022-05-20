import requests
import json
import pandas as pd


if __name__=="__main__":

    item_per_page = 200

    lst_alphabetes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    for alphabete in lst_alphabetes:
        lst_item = []
        for i in range(1, 50):

            r = requests.get(r'https://drugbank.vn/services/drugbank/api/public/thuoc?page={}&size={}&tenThuoc={}&sort=rate,desc&sort=tenThuoc,asc'.format(i, item_per_page, alphabete))
            item_json_lst = json.loads(r.text)
            if len(item_json_lst) == 0:
                break

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
        df.to_csv('../../utils/data/drugbankvn_{}.csv'.format(alphabete))
