import json
import boto3

def lambda_handler(event, context):
    print('Get book details')
    print("Received event: " + json.dumps(event, indent=2))
    
    # isbn = "195153448"
    user_id = event["queryStringParameters"]['user_id'] if 'user_id' in event["queryStringParameters"] else ''
    isbn = event["queryStringParameters"]['isbn'] if 'isbn' in event["queryStringParameters"] else ''
    rate = event["queryStringParameters"]['rate'] if 'rate' in event["queryStringParameters"] else ''
    
    region = 'us-east-2'
    table_name = 'Ratings'
    dynamodb = boto3.client('dynamodb', region_name = region)
    
    key = {}
    key['User-ID'] = {'S':user_id}
    key['ISBN'] = {'S':isbn}
    key['Book-Rating'] = {'S':rate}
    response = dynamodb.put_item(
        TableName = table_name,
        Item = key
    )
    
    print("Received event: " + json.dumps(response, indent=2))
    if response['ResponseMetadata']["HTTPStatusCode"] == 200:
        return {
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Headers': '*',
                'Access-Control-Allow-Methods': 'PUT,POST,GET,OPTIONS',
                'Access-Control-Allow-Origin': '*',
                'X-Requested-With': '*'
            },
            'statusCode': 200
        }
    else:
        status_code = 400
        return {
            'statusCode': status_code,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Headers': '*',
                'Access-Control-Allow-Methods': 'PUT,POST,GET,OPTIONS',
                'Access-Control-Allow-Origin': '*',
                'X-Requested-With': '*'
            },
            'body': json.dumps('Not able to rate a book!')
        }

    

