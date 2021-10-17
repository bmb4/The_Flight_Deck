from logging import NullHandler
import os
import pymongo
from flask import Flask, request, render_template, flash

password = os.environ.get('DB_PASSWORD')

client = pymongo.MongoClient("mongodb+srv://bmb4:"+password+"@Four-in-a-Sequence.3v48s.mongodb.net/DB?retryWrites=true&w=majority")

db = client["DB"]
test = db["Test"]




app = Flask(__name__)
app.config['SECRET_KEY'] = "really secret key"

@app.route('/')
def index():
    return render_template('Login page.html')

   
@app.route('/Login Page',methods = ['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    userlist = test.find({"username":username})
    FailMessage = ("Invalid username or password")
    SuccessMsg = ("Login Success")
    if len(list(userlist)) == 0:
        mydict = { "username": username, "password": password}
        user = test.insert_one(mydict)
        return FailMessage
    else:
        print(len(list(userlist)))
        flash('Username is already taken')
        #return render_template('Login Page.html')
        return SuccessMsg 


if __name__ == '__main__':
    app.run(debug=True)