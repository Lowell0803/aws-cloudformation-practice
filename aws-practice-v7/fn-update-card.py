import json
import boto3

def lambda_handler(event, context):
    request_body = json.loads(event['body'])
    update_card_status(request_body['card_no'], request_body['status'])

    return {
        'statusCode': 200,
        'body': json.dumps(f"Card {request_body['card_no']} status has been updated to {request_body['status']}.")
    }

def update_card_status(card_no, status):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('card_account_cfn')
    table.update_item(
        Key={'card_no': card_no},
        UpdateExpression="SET #s = :s",
        ExpressionAttributeNames={'#s': 'status'},
        ExpressionAttributeValues={':s': status},
        ReturnValues="UPDATED_NEW"
    )
