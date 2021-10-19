from logging import NullHandler
import os
import pymongo
from flask import Flask, request, render_template, flash
import main

password = os.environ.get('DB_PASSWORD')

client = pymongo.MongoClient("mongodb+srv://bmb4:"+password+"@Four-in-a-Sequence.3v48s.mongodb.net/DB?retryWrites=true&w=majority")

db = client["DB"]
test = db["Test"]




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
    userlist = test.find({"username":username})
    if password != passsword2:
        flash('Passwords do not match')
        return render_template('CreateAccount.html') 
    if len(list(userlist)) == 0:
        mydict = { "username": username, "password": password}
        user = test.insert_one(mydict)
        # keeping track of current logged in users                      # COMMENTED OUT FOR LATER USE
        # main.addressToUsername[request.remote_address] = username
        # main.usernameToAddress[username] = request.remote_address     # implemented for logging out
        return Message
    else:
        print(len(list(userlist)))
        flash('Username is already taken')
        return render_template('CreateAccount.html') 


if __name__ == '__main__':
    app.run(debug=True)
