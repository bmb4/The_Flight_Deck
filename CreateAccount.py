from logging import NullHandler
import os
import pymongo
import re
from flask import Flask, request, render_template, flash
import User
import responses
import DbHandler

password = os.environ.get('DB_PASSWORD')

client = pymongo.MongoClient("mongodb+srv://bmb4:"+str(password)+"@Four-in-a-Sequence.3v48s.mongodb.net/DB?retryWrites=true&w=majority")

db = client["DB"]
UserAccounts = db["UserAccounts"]

#
# app = Flask(__name__)
# app.config['SECRET_KEY'] = "really secret key"
#
# @app.route('/createaccount', methods = ['GET'])
# def index():
#     return render_template('CreateAccount.html')

#
# @app.route('/createaccount',methods = ['POST'])
def createaccount(form):
    username = form['username']
    password = form['password']
    passsword2 = form['password_confirm']
    if password != passsword2:

        return responses.create301("/signup")
    if len(password) < 6 or not re.search("^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[-+_!@#$%^&*.,?]).+", password):
        return responses.create301("/signup")
    if not DbHandler.nameExists(username):
        newUser = User.User(username, password)
        DbHandler.saveUser(newUser)
        return responses.create301("/landingpage")
    else:
        return responses.create301("/signup")


if __name__ == '__main__':
    app.run(debug=True)
