import json
import boto3
# Get DB
dynamodb = boto3.resource('dynamodb')

UserTable = dynamodb.Table('FinalDB')
AllUSers = UserTable.scan()

def lambda_handler(event, context):
    
        
    params = event['queryStringParameters']
    # params = {"accountName": "me"}

    
    AccountName = params['accountName']
    
    for item in AllUSers['Items']:
        if item['Account name'] == AccountName:
            return {
                'statusCode': 200,
                'body': json.dumps(item, cls = JsonDecimalToInt)
            }
    
    # return {
    #     'statusCode': 200,
    #     'body': json.dumps(AllUSers, cls = JsonDecimalToInt)
    # }




class JsonDecimalToInt(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, decimal.Decimal):
            return int(obj)
        return super(JsonDecimalToInt, self).default(obj)