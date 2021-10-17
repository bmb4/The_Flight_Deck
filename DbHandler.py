import pymongo
import User as u

myClient = pymongo.MongoClient("mongodb://mongo:27017/")
db = myClient["db"]
users = db["users"]

def saveUser(user):
    users.insert_one(user.asDict())

def nameExists(name):
    user = users.find({"username":name})
    if len(list(user)) != 0:
        return True
    return False

def getUser(name):
    user = users.find_one({"username": name})
    username = user["username"]
    password = user["password"]
    stats = user["stats"]

    newUser = u.User(username, password)
    newUser.stats = stats
    return newUser

def updateUser(user):
    name = user.username
    users.delete_one({"username": name})
    saveUser(user)

def getLeaders():
    for doc in users.find().sort('wins', pymongo.DESCENDING):
        print(doc)



