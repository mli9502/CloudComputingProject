import json
import boto3

def lambda_handler(event, context):
    # TODO implement
    # return {
    #     'statusCode': 200,
    #     'body': json.dumps('Hello from Lambda!')
    # }
    print('Search bookstore')
    print("Received event: " + json.dumps(event, indent=2))
    
    user_id = event["queryStringParameters"]['user_id'] if 'user_id' in event["queryStringParameters"] else ''
    print('Search bookstore for user ', user_id)
    
    region = 'us-east-2'
    dynamodb = boto3.client('dynamodb', region_name = region)
    
    table_name = 'Users'
    key = {}
    key['User-ID'] = {'S':user_id}
    user_response = dynamodb.get_item(
        TableName = table_name,
        Key = key
    )
    print('user search done')
    print("user search result: " + json.dumps(user_response, indent=2))
    user_area = user_response['Item']['Location']['S']
    print('user location is ' + user_area)
    
    location = boto3.client('location', region_name=region)
    location_response = location.search_place_index_for_suggestions(
        IndexName='IndexForBookstores',
        MaxResults=5,
        Text= "bookstore in " + user_area
    )
    
    print('bookstore search done')
    print("Bookstore search result: " + json.dumps(location_response, indent=2))
    
    if len(location_response["Results"]) == 0:
        status_code = 400
        return {
            'statusCode': status_code,
            'body': json.dumps('The area is not searchable!')
        }
    final_list = []
    for places in location_response["Results"]:
        if len(places['Text'].split(",")) > 4:
            final_list.append(places)
    
    print(final_list)
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
            "results": final_list
        }),
        "isBase64Encoded": False
    }
