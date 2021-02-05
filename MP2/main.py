from flask import Flask, request, g
import json
import os 


app = Flask(__name__)



# url = 'https://seorwrpmwh.execute-api.us-east-1.amazonaws.com/prod/mp1'

# payload = {
# 		'ip_address1':  # <insert ip address:port of first EC2 instance>, 
# 		'ip_address2':  # <insert ip address:port of secong EC2 instance>,
# 		'load_balancer' :  # <insert address of load balancer>,
# 		'submitterEmail':  # <insert your coursera account email>,
# 		'secret':  # <insert your secret token from coursera>
# 		}

# r = requests.post(url, data=json.dumps(payload))

# print(r.status_code, r.reason)
# print(r.text)
 
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

