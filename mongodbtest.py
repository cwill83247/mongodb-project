import os     # this is from a Youtube Tutorial on how to connect 
import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://cwill:MeanStackCW@atlascluster.etmsd74.mongodb.net/?retryWrites=true&w=majority")


DATABASE = cluster["my1stMongoDB"]
COLLECTION = DATABASE["celebrities"]


results = COLLECTION.find()


for result in results:
    print(result)


