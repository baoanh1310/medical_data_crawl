import os
import pandas as pd

data_list = os.listdir('../data')
data_path_list = [os.path.join('../data', name) for name in data_list]

df_list = [pd.read_csv(path) for path in data_path_list]

df_merge = pd.concat(df_list)
df_merge = df_merge.drop_duplicates(subset=['id'], keep='last')
df_merge = df_merge.drop_duplicates(subset=['tenThuoc'], keep='last')
print("Merge info: ")
print(df_merge.info())

df_merge.to_csv('./drugbank_clean.csv')