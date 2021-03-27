import requests
import json

url = 'https://ikm2evu584.execute-api.us-east-1.amazonaws.com/test/mp11-autograder'

payload = {
			"submitterEmail": "orihara2@illinois.edu", # <insert your coursera account email>,
			"secret": "Vf1oCeTPt5wXO1Ik", # <insert your secret token from coursera>,
			# "partId" : "G6U3L"
			"dbApi": "https://zb11vbo5fe.execute-api.us-east-2.amazonaws.com/mp6_stage"
		}
print(json.dumps(payload))
r = requests.post(url, data=json.dumps(payload))

print(r.status_code, r.reason)
print(r.text)