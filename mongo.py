import os
import pymongo

if os.path.exists("env.py"):    #this line is basically saying if its env.py then its local so use local environment variables
    import env

MONGO_URI = os.environ.get("MONGO_URI")       #referencing the MOMGO_URI in env.py    
DATABASE = "my1stMongoDB"
COLLECTION = "celebrities"

def mongo_connect(url):                 #function for mongo expecting 1 paramater to be passed in when it gets called/invoked
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected")
        return conn
    except pymongo.errors.ConnectionFailure as e:              #std for errors
        print("Could not connect to MongoDB: %s") % e


conn = mongo_connect(MONGO_URI)                           #std  calls function and passes in uri

coll = conn[DATABASE][COLLECTION]                        #STD PASSED IN VARIABLES FORM ABOVE 

documents = coll.find()                       

for doc in documents:
    print(doc)