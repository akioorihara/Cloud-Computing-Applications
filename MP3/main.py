from flask import Flask, request, g
import json
import os 


app = Flask(__name__)
 
seed = 0 
@app.route('/' , methods=['GET','POST'])
def getNumber():

    global seed 
    if request.method == 'GET':
        return str(seed)

    if request.method == 'POST':  #Trying to post it but do we need a form in html to input? 
        data = request.get_json()
        seed = data['num']
        return str(seed)
 
    return "Done"

