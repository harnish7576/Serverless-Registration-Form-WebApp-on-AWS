import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('form-table')

def lambda_handler(event, context):
    print(event)

    response = table.put_item(
        Item={
            'email': event['email'],
            'name': event['name'],
            'phone': event['phone'],
            'password': event['password']
        }
    )

    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps({'message': 'Registration successful'})
    }