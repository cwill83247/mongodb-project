import os
import pymongo

if os.path.exists("env.py"):    # this line is basically saying if its env.py then its local so use local environment variables
    import env

MONGO_URI = os.environ.get("MONGO_URI")       # referencing the MOMGO_URI in env.py    
DATABASE = "my1stMongoDB"
COLLECTION = "celebrities"

def mongo_connect(url):                 # function for mongo  to connect to db expecting 1 paramater to be passed in when it gets called/invoked
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected")
        return conn
    except pymongo.errors.ConnectionFailure as e:              # std for errors
        print("Could not connect to MongoDB: %s") % e


def show_menu():                                               # this is a 
    print("")
    print("1. Add a record")
    print("2. Find a record by name")
    print("3. Edit a record")
    print("4. Delete a record")
    print("5. Exit")

    option = input("Enter option: ")              # this is input prompt
    return option                                   # this returns the option the user has input

def get_record():                           #created as a HELPER FUNCTION to use with other functions so not repeating code so get sthe record for delete update etc.. 
    print("")
    first = input("Enter first name > ")    #takes users input
    last = input("Enter last name > ")

    try:
        doc = coll.find_one({"first": first.lower(), "last": last.lower()})       # using the coll option
    except:
        print("Error accessing the database")

    if not doc:
        print("")
        print("Error! No results found.")

    return doc


def add_record():
    print("")
    first = input("Enter first name > ")      # creating first name variable that takes the users input 
    last = input("Enter last name > ")
    dob = input("Enter date of birth > ")
    gender = input("Enter gender > ")
    hair_color = input("Enter hair color > ")
    occupation = input("Enter occupation > ")
    nationality = input("Enter nationality > ")

    new_doc = {                                 # variable new_doc for  building dictonairy
        "first": first.lower(),             # adding variables from above    the 2nd first -- 
        "last": last.lower(),
        "dob": dob,
        "gender": gender,
        "hair_color": hair_color,
        "occupation": occupation,
        "nationality": nationality
    }

    try:                                    
        coll.insert(new_doc)                              #trying to insert the above dictonairy into the collection...    is coll just standard syntax ?? 
        print("")
        print("Document inserted")
    except:
        print("Error accessing the database")


def find_record():
    doc = get_record()                              #calling the helper function
    if doc:
        print("")
        for k, v in doc.items():
            if k != "_id":
                print(k.capitalize() + ": " + v.capitalize())       # k is for the key and v is for the value, could have been any letters 


def edit_record():
    doc = get_record()
    if doc:
        update_doc = {}                     #creating a dictonairy to store the vlaues temporarily until we add 
        print("")
        for k, v in doc.items():
            if k != "_id":
                update_doc[k] = input(k.capitalize() + " [" + v + "] > ")

                if update_doc[k] == "":
                    update_doc[k] = v

        try:
            coll.update_one(doc, {"$set": update_doc})
            print("")
            print("Document updated")
        except:
            print("Error accessing the database")


def delete_record():
    doc = get_record()
    if doc:
        print("")
        for k, v in doc.items():
            if k != "_id":
                print(k.capitalize() + ": " + v.capitalize())

        print("")
        confirmation = input("Is this the document you want to delete?\nY or N > ")
        print("")

        if confirmation.lower() == "y":
            try:
                coll.remove(doc)
                print("Document deleted!")
            except:
                print("Error accessing the database")
        else:
            print("Document not deleted")


def main_loop():
    while True:
        option = show_menu()
        if option == "1":
            add_record()
        elif option == "2":
            print("You have selected option 2")
        elif option == "3":
            print("You have selected option 3")
        elif option == "4":
            print("You have selected option 4")
        elif option == "5":
            conn.close()                                #this closes 
            break
        else:
            print("Invalid option")
        print("")


conn = mongo_connect(MONGO_URI)                           #std  calls function and passes in uri

coll = conn[DATABASE][COLLECTION]                        #STD PASSED IN VARIABLES FORM ABOVE 
main_loop()                                               #calling function

