# import urllib.request as requests
from urllib import request, parse
import json
import uuid

# import requests

url = "https://seorwrpmwh.execute-api.us-east-1.amazonaws.com/prod/mp2"

hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,/;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

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
data = parse.urlencode(payload).encode()
r = request.Request(url, headers=hdr)
srp = request.urlopen(r).read()
print(srp.status_code, srp.reason)
print(srp.text)