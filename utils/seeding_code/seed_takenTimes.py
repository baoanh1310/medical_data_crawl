from pymongo import MongoClient
import pandas as pd

if __name__ == '__main__':
    MONGODB_URI = "mongodb://baoanh:baoanh@localhost:27017"
    MONGODB_DATABASE = 'vaipeapis'
    CRAWLER_COLLECTION = "takentimes"

    connection = MongoClient(MONGODB_URI)
    db = connection[MONGODB_DATABASE]
    collection = db.database[CRAWLER_COLLECTION]

    # get list data
    hours = [ { "hour": hour } for hour in range(24) ]
    lst_data = []
    for hour in range(24):
        for minute in range(60):
            el = { "hour": hour, "minute": minute }
            lst_data.append(el)
    print(len(lst_data))
    assert(len(lst_data) == 24 * 60)
    collection.insert_many(lst_data)
