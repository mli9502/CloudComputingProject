import json
import boto3
from random import randint
from boto3.dynamodb.conditions import Key

def get_random_primary_keys():
    region = 'us-east-2'
    table_name = 'Books'
    dynamodb = boto3.resource('dynamodb', region_name = region)
    table = dynamodb.Table(table_name)
    num_iter = 0
    while True:
        if num_iter > 100:
            break
        rnd = randint(166789222, 966789222)
        # print(rnd)
        r = table.scan(
            Limit=50,
            TableName=table_name,
            FilterExpression=Key('ISBN').gt(str(rnd))
        )
        if r['Count'] == 0:
            num_iter += 1
            continue
        return r['Items']
    return None

def get_unique_random_primary_keys(num_books = 10):
    rand_isbns = set()
    rtn = []
    while len(rand_isbns) < num_books:
        tmp_keys = get_random_primary_keys()
        if tmp_keys is None:
            continue
        # print(rand_isbns)
        for tmp in tmp_keys:
            # print(tmp)
            if tmp['ISBN'] in rand_isbns:
                # print('skipping ' + tmp['ISBN'])
                continue
            rand_isbns.add(tmp['ISBN'])
            rtn.append(tmp)
            if len(rand_isbns) == num_books:
                break
    print(rand_isbns)
    print('\n')
    return rtn

def lambda_handler(event, context):
    print("Received event: " + json.dumps(event, indent=2))
    user_id = event["queryStringParameters"]['user_id'] if 'user_id' in event["queryStringParameters"] else ''
    print('Recommnd book for user ', user_id)
   
    if user_id == '':
        return {
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Headers': '*',
                'Access-Control-Allow-Methods': 'PUT,POST,GET,OPTIONS',
                'Access-Control-Allow-Origin': '*',
                'X-Requested-With': '*'
            },
            'statusCode': status_code,
            'body': json.dumps('user id should be provided!')
        }
    else:
        print(user_id)
        rand_primary_key = get_unique_random_primary_keys()
        print(rand_primary_key)

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
                "results": get_unique_random_primary_keys()
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
