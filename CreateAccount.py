from logging import NullHandler
import os
import pymongo
from flask import Flask, request, render_template, flash
import User
import responses

password = os.environ.get('DB_PASSWORD')

client = pymongo.MongoClient("mongodb+srv://bmb4:"+password+"@Four-in-a-Sequence.3v48s.mongodb.net/DB?retryWrites=true&w=majority")

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
    username = form['username'].decode()
    password = form['password'].decode()
    passsword2 = form['password_confirm'].decode()
    Message =("Account Created!!!<br> username: "+username+"<br>password: "+ password)
    userlist = UserAccounts.find({"username":username})
    if password != passsword2:
        flash('Passwords do not match')
        return responses.create301("/signup")
    if len(list(userlist)) == 0:
        newUser = User.User(username, password)
        UserAccounts.insert_one(newUser.asDict())
        return responses.create301("/landingpage")
    else:
        print(len(list(userlist)))
        return responses.create301("/signup")


if __name__ == '__main__':
    app.run(debug=True)
