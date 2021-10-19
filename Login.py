from logging import NullHandler
import os
import pymongo
import responses


password = os.environ.get('DB_PASSWORD')

client = pymongo.MongoClient("mongodb+srv://bmb4:"+str(password)+"@Four-in-a-Sequence.3v48s.mongodb.net/DB?retryWrites=true&w=majority")

db = client["DB"]
test = db["UserAccounts"]


def login(form):
    username = form['username']
    password = form['password']
    userlist = test.find({"username":username})
    FailMessage = ("Invalid username or password")
    if len(list(userlist)) == 0:
        return FailMessage
    elif password != userlist[0]['password']:
        return FailMessage
    elif password ==  userlist[0]['password']:
            #route to landing or profile page
            return responses.create301("/landingpage")
    else:
        return ("unknown error")


