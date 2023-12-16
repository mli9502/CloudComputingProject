import json
import boto3

def lambda_handler(event, context):
    # TODO implement
    user_id = event["queryStringParameters"]['user_id'] if 'user_id' in event["queryStringParameters"] else ''
    
    region = 'us-east-2'
    table_name = 'Ratings'
    dynamodb = boto3.client('dynamodb', region_name = region)
    
    key = {}
    key['User-ID'] = {'S':user_id}
    
    response=dynamodb.query(
        ExpressionAttributeNames={
            "#UserID":"User-ID",
        },
        ExpressionAttributeValues={
            ':user_id': {
                'S': user_id,
            },
        },
        KeyConditionExpression='#UserID =:user_id',
        TableName=table_name
    )
    
    print("Received event: " + json.dumps(response, indent=2))
    return {
            "statusCode": 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Headers': '*',
                'Access-Control-Allow-Methods': 'PUT,POST,GET,OPTIONS',
                'Access-Control-Allow-Origin': '*',
                'X-Requested-With': '*'
            },
            "body": json.dumps({
                "results": response['Items']
            }),
            "isBase64Encoded": False
        }
