import requests
import json

url = 'https://seorwrpmwh.execute-api.us-east-1.amazonaws.com/prod/mp1'

payload = {
		'ip_address1': '52.207.216.180', # <insert ip address:port of first EC2 instance>, 
		'ip_address2':  '3.84.39.12', # <insert ip address:port of secong EC2 instance>,
		'load_balancer' : 'mp2LB-1956518224.us-east-1.elb.amazonaws.com', # <insert address of load balancer>,
		'submitterEmail':  'orihara2@illinois.edu', # <insert your coursera account email>,
		'secret': 'ZagevsDkmc0bXjfb' # <insert your secret token from coursera>
		}

r = requests.post(url, data=json.dumps(payload))

print(r.status_code, r.reason)
print(r.text)