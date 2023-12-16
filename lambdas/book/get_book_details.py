import json
import boto3

def lambda_handler(event, context):
    print('Get book details')
    print("Received event: " + json.dumps(event, indent=2))
    
    
    # isbn = "195153448"
    isbn = event["queryStringParameters"]['isbn'] if 'isbn' in event["queryStringParameters"] else ''

    region = 'us-east-2'
    table_name = 'Books'
    s3 = boto3.client('s3')
    dynamodb = boto3.client('dynamodb', region_name = region)
    
    key = {}
    if isbn != "":
        key['ISBN'] = {'S':isbn}
        response = dynamodb.get_item(
            TableName = table_name,
            Key = key
        )
        print('book search done')
        print("Book search result: " + json.dumps(response, indent=2))

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
                "results": response['Item']
            }),
            "isBase64Encoded": False
        }
    else:
        status_code = 400
        return {
            'statusCode': status_code,
            'body': json.dumps('This is an exception!')
        }
