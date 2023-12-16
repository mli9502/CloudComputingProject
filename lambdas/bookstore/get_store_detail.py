import json
import boto3


def lambda_handler(event, context):
    # TODO implement
    # return {
    #     'statusCode': 200,
    #     'body': json.dumps('Hello from Lambda!')
    # }

    print('Get bookstore detail')
    print("Received event: " + json.dumps(event, indent=2))
    
    place_id = event["queryStringParameters"]['place_id'] if 'place_id' in event["queryStringParameters"] else ''
    print('Search bookstore for ', place_id)
    
    region = 'us-east-2'
    location = boto3.client('location', region_name=region)
    place_response = location.get_place(
        IndexName='IndexForBookstores',
        PlaceId=place_id
    )
    
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
            "results": place_response['Place']
        }),
        "isBase64Encoded": False
    }
