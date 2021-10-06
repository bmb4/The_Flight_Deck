""" #import random
import pymongo

myClient = pymongo.MongoClient("mongodb://mongo:27017/")
db = myClient["db"]
numbers = db["numbers"]

def addRandomNumber():
    newNum = (random.random() * 100).__trunc__()
    print("New Number: ", newNum)
    numbers.insert_one({"num" : newNum})
    return

def showAllNums():
    print("All numbers: ")
    for num in numbers.find():
        print(num['num'])
    return

if __name__ == '__main__':
    addRandomNumber()
    showAllNums()
    print("Test") """