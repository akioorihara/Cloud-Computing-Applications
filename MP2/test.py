from flask import Flask, request
import random 


app = Flask(__name__)

@app.route('/' , methods=['GET', 'POST'])
def getNum():
    if request.method == 'POST':
        return 0
    random.seed(0)
    r = str(random.random())
    return r

@app.route('/')
def postNum():
    pass