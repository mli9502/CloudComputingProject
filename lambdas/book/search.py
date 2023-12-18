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
    
    key={}
    values = {}
    names = {}
    expression = ""
    if isbn != "":
        key['ISBN'] = {'S':isbn}
        response = dynamodb.get_item(
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
        
    else:
        if title != "":
            values[':booktitle'] = {'S':title}
            names['#booktitle'] = 'Book-Title'
            expression += "#booktitle = :booktitle"
        if author != "":
            values[':bookauthor'] = {'S':author}
            names['#bookauthor'] = 'Book-Author'
            if expression != "":
                expression += " and "
            expression += "#bookauthor = :bookauthor"
        if publish_year != "":
            values[':publishyear'] = {'S':publish_year}
            names['#publishyear'] = 'Year-Of-Publication'
            if expression != "":
                expression += " AND "
            expression += "#publishyear = :publishyear"
        if publisher != "":
            values[':publisher'] = {'S':publisher}
            names['#publisher'] = 'Publisher'
            if expression != "":
                expression += " and "
            expression += "#publisher = :publisher"
        if title == "" and author == "" and publish_year == "" and publisher == "":
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
                    "results": "Enter the filter conditions before search!"
                }),
                "isBase64Encoded": False
            }
        print("expressionL:" + expression)
        print("values:" + str(values))
        print("names:" + str(names))
        response = dynamodb.scan(
            TableName = table_name,
            FilterExpression = expression,
            ExpressionAttributeNames = names,
            ExpressionAttributeValues = values,
        )
        print('book search scan done')
        print("Book search scan result: " + json.dumps(response, indent=2))

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
