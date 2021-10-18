import json

import pymongo
import User as u
import os

password = str(os.environ.get('DB_PASSWORD'))
myClient = pymongo.MongoClient("mongodb+srv://bmb4:"+password+"@Four-in-a-Sequence.3v48s.mongodb.net/DB?retryWrites=true&w=majority")
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
    return users.find().sort('wins', pymongo.DESCENDING)

# def allUsers():
#     cursor = users.find({})
#     out = list()
#     for user in cursor:
#         out.append(getUser(user['username']).asDict())
#     return json.dump(out)