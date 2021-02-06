import requests
import json
import uuid

url = "https://seorwrpmwh.execute-api.us-east-1.amazonaws.com/prod/mp2"

payload = {
	"graphApi": #<post api for storing the graph>,
    "botName": # <name of your Amazon Lex Bot>, 
	"botAlias": # <alias name given when publishing the bot>,
    "identityPoolId": #<cognito identity pool id for lex>,
    "accountId": #<your aws account id used for accessing lex>,
	"submitterEmail": # <insert your coursera account email>,
	"secret": # <insert your secret token from coursera>
    }

r = requests.post(url, data=json.dumps(payload))

print(r.status_code, r.reason)
print(r.text)