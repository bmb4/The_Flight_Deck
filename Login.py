from logging import NullHandler
import os
import pymongo
import responses
import DbHandler


password = os.environ.get('DB_PASSWORD')

client = pymongo.MongoClient("mongodb+srv://bmb4:"+str(password)+"@Four-in-a-Sequence.3v48s.mongodb.net/DB?retryWrites=true&w=majority")

db = client["DB"]
test = db["UserAccounts"]


def login(form):
    username = form['username']
    password = form['password']
    if not DbHandler.nameExists(username):
        return responses.create301("/login")
    else :
        correctUser = DbHandler.getUser(username)
        if correctUser.password == password:
            #route to landing or profile page
            return responses.create301("/landingpage", 'Set-Cookie: user='+username+'\r\n')
        else:
            return responses.create301("/login")


