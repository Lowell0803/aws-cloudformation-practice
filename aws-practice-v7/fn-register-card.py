import json
import boto3

def lambda_handler(event, context):
    request_body = json.loads(event["body"])
    register_card(request_body)

    return {
        'statusCode': 200,
        'body': json.dumps(f"Card {request_body['card_no']} has been registered.")
    }

def register_card(item):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('card_account_cfn')
    item['status'] = 'INACTIVE'
    item['balance'] = 0
    table.put_item(Item=item)
