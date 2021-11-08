from logging import NullHandler
import os
import pymongo
import responses
import DbHandler


password = os.environ.get('DB_PASSWORD')

client = pymongo.MongoClient("mongodb+srv://bmb4:"+str(password)+"@Four-in-a-Sequence.3v48s.mongodb.net/DB?retryWrites=true&w=majority")

db = client["DB"]
test = db["UserAccounts"]


def login(self, form):
    username = form['username']
    password = form['password']
    if not DbHandler.nameExists(username):
        return responses.create301("/login")
    else :
        correctUser = DbHandler.getUser(username)
        if correctUser.password == password:
            #route to landing or profile page
            #also add username and address to dicts
            self.addressToUser[self.client_address[0]] = username
            self.userToAddress[username] = self.client_address[0]

            return responses.create301("/landingpage")
            return responses.create301("/landingpage")
        else:
            return responses.create301("/login")


