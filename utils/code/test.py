import os
import pandas as pd

filepath = './drugbank_clean.csv'
df = pd.read_csv(filepath)

new_df = pd.DataFrame()

new_df['id'] = df['id']
new_df['drugName'] = df['tenThuoc']
new_df['registerCode'] = df['soDangKy']
new_df['drugPropertyNames'] = df['hoatChat']
new_df['drugProperties'] = df['taDuoc']
new_df['category'] = df['phanLoai']
new_df['country'] = df['nuocSx']
new_df['addressFrom'] = df['diaChiSx']
new_df['registerAddress'] = df['diaChiDk']
new_df['registerCompany'] = df['congTyDk']
new_df['price'] = df['giaKeKhai']
new_df['expired'] = df['tuoiTho']
new_df['standard'] = df['tieuChuan']
new_df['drugType'] = df['nhomThuoc']
new_df['drugNum'] = df['soQuyetDinh']

# print(new_df.columns)
new_df.to_csv('./drugs.csv')