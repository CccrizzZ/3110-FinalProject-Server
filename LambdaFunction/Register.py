import json
import boto3

    


def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')

    UserTable = dynamodb.Table('FinalDB')
    AllUSers = UserTable.scan()
    params = event['queryStringParameters']
    # params = {"accountName": "og", "password": "1243"}
    
    # AccountName = ""
    # Password = ""
    # AccountName = event['accountName']
    # Password = event['password']
    
    AccountName = params['accountName']
    Password = params['password']
    
    print(AccountName)
    print(Password)
    
    user_exist = False
    
    
    # If input empty
    if(AccountName == "" or Password == ""):
        return{
            'statusCode': 200,
            'body': json.dumps("Please enter account name and password")
        }
    # Compare to existing names in the table
    for item in AllUSers['Items']:
        if item['Account name'] == AccountName:
            user_exist = True
            print("UserExist")
            return {
                'statusCode': 200,
                'body': json.dumps("User already exist")
                # 'body': json.dumps(event["queryStringParameters"])
            }
    
    
    if not user_exist:   
        # Register user in db
        UserTable.put_item(
          Item = {
                'Account name': AccountName,
                'Password': Password,
                'Level': "0",
                'Kill': "0",
                "Death": "0"
            }
        )
        
        return {
            'statusCode': 200,
            'body': json.dumps("Registration success")
        }
    else:
        
        return {
            'statusCode': 200,
            'body': json.dumps("User already exist")
        }
