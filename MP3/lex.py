import json
from pprint import pprint
import boto3
from botocore.exceptions import ClientError
import logging
from decimal import Decimal

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

def elicit_slot(session_attributes: dict, intent_name: str, slots: dict, slot_to_elicit: str):
    return {
        'sessionAttributes': session_attributes,
        'dialogAction': {
            'type': 'ElicitSlot',
            'intentName': intent_name,
            'slots': slots,
            'slotToElicit': slot_to_elicit
        }
    }

def close(session_attributes, fulfillment_state, message):
    response = {
        "sessionAttributes": session_attributes,
        "dialogAction": {
            "type": "Close",
            "fulfillmentState": fulfillment_state,
            "message": message
        }
    }

    return response

def form_message(message_text: str):
    return {
        "contentType": "PlainText",
        "content": message_text
    }



def lambda_handler(event, context):
    logger.debug("event.bot.name={}".format(event["bot"]["name"]))
    logger.debug("event=" + json.dumps(event))
    
    dynamodb = boto3.resource('dynamodb')
    client = boto3.client('dynamodb')
    table = dynamodb.Table('MP3')
    
    # slots = event["currentIntent"]["slots"]
    # distance = 1

    # for slot_name, slot_value in slots.items():
    #   if slot_value is None:
    #     return elicit_slot(event['sessionAttributes'], event['currentIntent'], slots, slot_name)
    #  #grab distance here
    #     print(slots)
    #   response = table.get_item(
    #     Key={
    #         'Source': src,
    #         'Destination': dest
    #     } 
    # return close(event['sessionAttributes'], "Fulfilled", form_message("The distance is"))
    
    print(event)
    src = event["currentIntent"]["slots"]["src"]
    # print(src)
    dest = event["currentIntent"]["slots"]["dest"]
    print(dest)
    
    response = table.get_item(
        Key={
            'Source': src,
            'Destination': dest
        }    
        
    )
    print(response['Item'], "----")
    
    
    response = {
        "dialogAction": {
            "type": "Close",
            "fulfillmentState": "Fulfilled",
            "message": {
              "contentType": "SSML",
              "content": (response['Item']['Distance']),
            },
        }
    }
    
    print('result = ' + str(response))
    return response
    
 

    
    # return {
    #     'statusCode': 200,
    #     'body': json.dumps('Hello from Lambda!')
    # }
