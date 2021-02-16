import requests
import json
import uuid

url = "https://seorwrpmwh.execute-api.us-east-1.amazonaws.com/prod/mp2"

payload = {
	"graphApi": 'https://uhaby07yy7.execute-api.us-east-1.amazonaws.com/test', #<post api for storing the graph>,
	"botName": 'CityDistance',# <name of your Amazon Lex Bot>, 
	"botAlias": 'citydist',# <alias name given when publishing the bot>,
	"identityPoolId": 'us-east-1:8018fa33-95ec-460a-8a6b-e92d6e7e0f95',#<cognito identity pool id for lex>,
	"accountId": '372078741047',#<your aws account id used for accessing lex>,
	"submitterEmail": 'orihara2@illinois.edu', # <insert your coursera account email>,
	"secret": '7uYQT6VruKQGog07',# <insert your secret token from coursera>,
	"region": 'us-east-1'#<Region where your lex is deployed (Ex: us-east-1)>
    }

r = requests.post(url, data=json.dumps(payload))

print(r.status_code, r.reason)
print(r.text)