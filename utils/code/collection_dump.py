from pymongo import MongoClient
import bson
import pandas as pd
import pytz
from datetime import datetime
import tzlocal

def convert_timestamp_in_datetime_utc(timestamp_received):
    local_timezone = tzlocal.get_localzone() # get pytz timezone
    return datetime.fromtimestamp(timestamp_received, local_timezone).strftime("%Y/%m/%d")

def convertColumnToNumeric(col):
    if type(col) == str:
        return float(col.replace(',', ''))
    return col


if __name__ == '__main__':
    MONGODB_URI = "mongodb://localhost:27017"
    MONGODB_DATABASE = 'vaipeapis'
    CRAWLER_COLLECTION = "drugs"

    connection = MongoClient(MONGODB_URI)
    db = connection[MONGODB_DATABASE]
    collection = db.database[CRAWLER_COLLECTION]
    cursor =  collection.find({})

    ## write to json
    # with open('full_data.json', 'w') as file:
    #     file.write('[')
    #     for document in cursor:
    #         file.write(dumps(document, ensure_ascii=False))
    #         file.write(',')
    #     file.write(']')

    # ------------------------------------
    # normalize chi tieu quan trong
    lst_dict = []
    for doc in cursor:
        # doc['Ngày Giao Dịch'] = convert_timestamp_in_datetime_utc(int(doc['Ngày Giao Dịch']) / 1000 )
        lst_dict.append(doc)

    df = pd.DataFrame(lst_dict)
    # cols  = ['Tổng tài sản', 'Vốn chủ sở hữu',
    #          'Doanh thu thuần', 'Lợi nhuận gộp', 'LN từ hoạt động SXKD',
    #          'Lợi nhuận sau thuế', 'Lợi ích cổ đông công ty mẹ',
    #          'Biên lãi gộp (trailing 4 quý) %', 'EPS (trailing 4 quý)',
    #          'ROA (trailing 4 quý) %', 'ROE (trailing 4 quý) %']
    # for col in cols:
    #     df_final[col] = df_final[col].apply(convertColumnToNumeric)
    df.to_csv('../data/drug_clean.csv', index=False)
    # ------------------------------------