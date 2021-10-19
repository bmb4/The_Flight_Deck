from logging import NullHandler
import os
import pymongo
from flask import Flask, request, render_template, flash
import User

password = os.environ.get('DB_PASSWORD')

client = pymongo.MongoClient("mongodb+srv://bmb4:"+password+"@Four-in-a-Sequence.3v48s.mongodb.net/DB?retryWrites=true&w=majority")

db = client["DB"]
UserAccounts = db["UserAccounts"]


app = Flask(__name__)
app.config['SECRET_KEY'] = "really secret key"

@app.route('/createaccount', methods = ['GET'])
def index():
    return render_template('CreateAccount.html')

   
@app.route('/createaccount',methods = ['POST'])
def createaccount():
    username = request.form['username']
    password = request.form['password']
    passsword2 = request.form['password_confirm']
    Message =("Account Created!!!<br> username: "+username+"<br>password: "+ password)
    userlist = UserAccounts.find({"username":username})
    if password != passsword2:
        flash('Passwords do not match')
        return render_template('CreateAccount.html') 
    if len(list(userlist)) == 0:
        newUser = User.User(username, password)
        UserAccounts.insert_one(newUser.asDict())
        return Message
    else:
        print(len(list(userlist)))
        flash('Username is already taken')
        return render_template('CreateAccount.html') 


if __name__ == '__main__':
    app.run(debug=True)
