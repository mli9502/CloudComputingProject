import json
import boto3

def lambda_handler(event, context):
    print('book search')
    print("Received event: " + json.dumps(event, indent=2))
    
    
    # isbn = "195153448"
    isbn = event["queryStringParameters"]['isbn'] if 'isbn' in event["queryStringParameters"] else ''
    title = event["queryStringParameters"]['title'] if 'title' in event["queryStringParameters"] else ''
    author = event["queryStringParameters"]['author'] if 'author' in event["queryStringParameters"] else ''
    publish_year = event["queryStringParameters"]['publish_year'] if 'publish_year' in event["queryStringParameters"] else ''
    publisher = event["queryStringParameters"]['publisher'] if 'publisher' in event["queryStringParameters"] else ''
    
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
    else:
        if title != "":
            key['Book-Title'] = {'S':title}
        if author != "":
            key['Book-Author'] = {'S':author}
        if publish_year != "":
            key['Year-Of-Publication'] = {'S':publish_year}
        if publisher != "":
            key['Publisher'] = {'S':publisher}
        response = dynamodb.query(
            TableName = table_name,
            Key = key
        )
    print('book search done')
    print("Book search result: " + json.dumps(response, indent=2))
    # return response['Item']
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
