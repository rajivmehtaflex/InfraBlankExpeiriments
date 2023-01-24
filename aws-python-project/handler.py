import json


def hello(event, context):
    
    body=json.loads(event['Records'][0]['body'])
    message=json.loads(body['Message'])    
    print(f'Data -->{message}')
    body = {
        "message": "Go Serverless v3.0! Your function executed successfully!"
    }

    return {"statusCode": 200, "body": json.dumps(body)}
