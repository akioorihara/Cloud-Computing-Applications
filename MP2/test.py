from flask import Flask, request, jsonify
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

@app.route('/json' , methods=['POST'])
def getNumber():
    
    # f = open("application/temp.json", "r")
    # value = json.load(f)
    print(request.is_json)
    req = request.get_json()
    print(req)

    return "Done"

