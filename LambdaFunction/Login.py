import json
import boto3

    


def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    UserTable = dynamodb.Table('FinalDB')
    AllUSers = UserTable.scan()
    
    params = event['queryStringParameters']
    # params = {"accountName": "test5", "password": "test5"}

    
    AccountName = params['accountName']
    Password = params['password']
    
    print(AccountName)
    print(Password)
    
    user_exist = False
    password_right = False
    
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
            if item['Password'] == Password:
                password_right =True    
    
    
    if user_exist and password_right:   
        
        return {
            'statusCode': 200,
            'body': json.dumps("Login success")
        }
    else:
        
        return {
            'statusCode': 200,
            'body': json.dumps("Wrong user name or password")
        }
