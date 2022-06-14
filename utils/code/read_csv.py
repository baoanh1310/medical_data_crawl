import pandas as pd

df = pd.read_csv('drugbank_clean.csv')
for col in df.columns:
    print(col)