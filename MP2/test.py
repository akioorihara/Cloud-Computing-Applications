from flask import Flask
import random 

app = Flask(__name__)

@app.route('/')
def getNum():
    random.seed(0)
    r = str(random.random())
    return r

@app.route('/')
def postNum():
    return "test"