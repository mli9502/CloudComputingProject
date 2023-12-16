import json

def lambda_handler(event, context):

    print("Received event: " + json.dumps(event, indent=2))
    user_id = event["queryStringParameters"]['user_id'] if 'user_id' in event["queryStringParameters"] else ''
    print('Recommnd book for user ', user_id)
   
    if user_id is '':
        return {
            'statusCode': status_code,
            'body': json.dumps('user id should be provided!')
        }
    else:
        #TODO: Remove below tmp, provide recommendation algorithm here -> input: user-id, return: a list of ISBN
        tmp = ["515116386", "316105368", "689113617", "812090241"]
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
                "results": tmp
            }),
            "isBase64Encoded": False
        }

    
    # user_id = event["queryStringParameters"]['user_id'] if 'user_id' in event["queryStringParameters"] else ''
    # if user_id is '':
    #     return {
    #         'statusCode': status_code,
    #         'body': json.dumps('user id should be provided!')
    #     }
    # else:
    #     region = 'us-east-2'
    #     table_name = 'Users'
    #     s3 = boto3.client('s3')
    #     dynamodb = boto3.client('dynamodb', region_name = region)
    
    #     key['User-ID'] = {'S':user_id}
    #     response = dynamodb.get_item(
    #         TableName = table_name,
    #         Key = key
    #     )
    #     print('User search done')
    #     print("User search result: " + json.dumps(response, indent=2))
    #     return {
    #         "statusCode": 200,
    #         'headers': {
    #             'Content-Type': 'application/json',
    #             'Access-Control-Allow-Headers': '*',
    #             'Access-Control-Allow-Methods': 'PUT,POST,GET,OPTIONS',
    #             'Access-Control-Allow-Origin': '*',
    #             'X-Requested-With': '*'
    #         },
    #         "body": json.dumps({
    #             "results": response['Item']
    #         }),
    #         "isBase64Encoded": False
    #     }
