from pymongo import MongoClient
import pandas as pd

if __name__ == '__main__':
    MONGODB_URI = "mongodb://baoanh:baoanh@localhost:27017"
    MONGODB_DATABASE = 'vaipeapis'
    CRAWLER_COLLECTION = "weekdays"

    connection = MongoClient(MONGODB_URI)
    db = connection[MONGODB_DATABASE]
    collection = db.database[CRAWLER_COLLECTION]

    # get list data
    lst_data = [ { "weekDay": num } for num in range(7) ]
    collection.insert_many(lst_data)