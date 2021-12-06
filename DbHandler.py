import json

import pymongo
import User as u
import os
from operator import itemgetter

password = str(os.environ.get('DB_PASSWORD'))
myClient = pymongo.MongoClient("mongodb+srv://bmb4:"+password+"@Four-in-a-Sequence.3v48s.mongodb.net/DB?retryWrites=true&w=majority")
db = myClient["DB"]
users = db["UserAccounts"]

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
    profile_pic = user["profile_pic"]

    newUser = u.User(username, password)
    newUser.stats = stats
    newUser.profile_pic = profile_pic
    return newUser

def updateUser(user):
    name = user.username
    users.delete_one({"username": name})
    saveUser(user)


def getLeaders():
    userlist = users.find({})
    #for doc in userlist: print(doc)
    userWins = [("Dummy", -1)]
    print(userWins)
    for user in userlist:
        name = user["username"]
        #print(name)
        wins = user["stats"]["Wins"]
        userWins.append((name,wins))
    userWins.sort(key=itemgetter(1),reverse=True)
    print(userWins)
    # userWins = [(user["username"],user["stats"]["Wins"]) for user in userlist].sort(key = lambda x: x[1])
    return userWins

def applyGameResults(isDraw, winner, loser):
    winner_info = getUser(winner).stats
    loser_info = getUser(loser).stats
    if isDraw:
        users.update({'username': winner}, {"$set": { 'stats.Draws': int(winner_info['Draws']) + 1, "stats.Games Played": int(winner_info['Games Played']) + 1 }})
        users.update({'username': loser}, {"$set": { 'stats.Draws': int(loser_info['Draws']) + 1, "stats.Games Played": int(loser_info['Games Played']) + 1 }})
    else:
        users.update({'username': winner}, {"$set": { 'stats.Wins': int(winner_info['Wins']) + 1, "stats.Games Played": int(winner_info['Games Played']) + 1 }})
        users.update({'username': loser}, {"$set": { 'stats.Losses': int(loser_info['Losses']) + 1, "stats.Games Played": int(loser_info['Games Played']) + 1 }})

if __name__ == '__main__':
    getLeaders()
# def allUsers():
#     cursor = users.find({})
#     out = list()
#     for user in cursor:
#         out.append(getUser(user['username']).asDict())
#     return json.dump(out)
