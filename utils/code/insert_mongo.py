from pymongo import MongoClient
import bson
import pandas as pd
# import pytz
from datetime import datetime

def getListRecords(df_file):
    df = pd.read_csv(df_file)
    df.drop(columns=['Unnamed: 0'], axis=1, inplace=True)
    df_final = df.fillna('')
    return df_final.to_dict("records")

if __name__ == '__main__':
    MONGODB_URI = "mongodb://baoanh:baoanh@localhost:27017"
    MONGODB_DATABASE = 'vaipeapis'
    CRAWLER_COLLECTION = "drugs"

    connection = MongoClient(MONGODB_URI)
    db = connection[MONGODB_DATABASE]
    collection = db.database[CRAWLER_COLLECTION]

    # get list data
    lst_data = getListRecords("../data/drugs.csv")
    collection.insert_many(lst_data)
    # print(lst_data[0])