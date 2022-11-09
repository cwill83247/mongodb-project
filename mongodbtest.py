import os
import pymongo
from pymongo import MongoClient

#cluster = MongoClient("mongodb+srv://cwill:MeanStackCW@atlascluster.etmsd74.mongodb.net/?retryWrites=true&w=majority")


DATABASE = cluster["my1stMongoDB"]
COLLECTION =DATABASE["celebrities"]

results = COLLECTION.find({"nationality":"british"})

for result in results:
    print(result)


