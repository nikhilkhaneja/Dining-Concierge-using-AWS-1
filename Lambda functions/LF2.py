import json
import boto3
import random
import requests
from requests_aws4auth import AWS4Auth

sender_email_addr = "rrr9293@nyu.edu"

def get_restaurants_from_elastic_search(cuisine):
    print("Searching for cuisine" + cuisine)
    region = 'us-west-2' 
    service = 'es'
    credentials = boto3.Session().get_credentials()
    awsauth = AWS4Auth(credentials.access_key, credentials.secret_key, region, service, session_token=credentials.token)
    
    host = 'https://search-diningconciergeold-y36aixk37hngct542nd7rrtojm.us-west-2.es.amazonaws.com/'
    index = 'restaurants'
    url = host + index + '/_search'
    query = {
        "size": 25,
        "query": {
            "multi_match": {
                "query": cuisine,
                "fields": ["categories"]
            }
        }
    }
    headers = { "Content-Type": "application/json" }
    r = requests.get(url, auth=awsauth, headers=headers, data=json.dumps(query))
    response = {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": '*'
        },
        "isBase64Encoded": False
    }
    response['body'] = r.text
    response['body'] = json.loads(response['body'])
    
    # Take a random restaurant based on cuisine and return its id
    matches = response['body']['hits']['hits']
    #print(response)
    restaurantIdList = random.choices(matches, k=5)
    restaurantIdList = [restaurant['_id'] for restaurant in random.choices(matches, k=5)]
    print(restaurantIdList)
    return restaurantIdList 
    

def get_restaurant_details_from_dynamo(restaurantIdList):
    dynamo = boto3.client('dynamodb')
    final_restaurant_List = []
    for restaurantId in restaurantIdList:
        response = dynamo.get_item(
            TableName="yelp-restaurants",
            Key={
                "RestaurantID": {
                    "S": restaurantId
                }
            }
        )
        final_restaurant_List.append(response['Item'])
    print(final_restaurant_List)
    return final_restaurant_List
    

def send_email_using_ses(restaurant_detail_set, email_addr, cuisine, location):
    ses = boto3.client('ses')
    verifiedResponse = ses.list_verified_email_addresses()
    if email_addr not in verifiedResponse['VerifiedEmailAddresses']:
        verifyEmailResponse = ses.verify_email_identity(EmailAddress=email_addr)
        return
    message = "Hi, Here is the list of top 5 {} restaurants at {} I found that mights suit you: ".format(cuisine, location)
    message_restaurant = ""
    count = 1
    for restaurant in restaurant_detail_set:
        restaurantName = restaurant['Name']['S']
        restaurantAddress = restaurant['Address']['S']
        restaurantZip = restaurant['ZipCode']['S']
        reviewCount = restaurant['TotalReviews']['N']
        ratings = restaurant['Rating']['N']
        message_restaurant += str(count)+". {} located at {}, {} with Ratings of {} and {} reviews. ".format(restaurantName, restaurantAddress, restaurantZip, ratings, reviewCount)
        message_restaurant += "\n"
        count += 1
    print(message_restaurant)
    # Send a mail to the user regarding the restaurant suggestions
    mailResponse = ses.send_email(
        Source=sender_email_addr,
        Destination={'ToAddresses': [email_addr]},
        Message={
            'Subject': {
                'Data': "Dining Conceirge Chatbot has a message for you!",
                'Charset': 'UTF-8'
            },
            'Body': {
                'Text': {
                    'Data': message+message_restaurant,
                    'Charset': 'UTF-8'
                },
                'Html': {
                    'Data': message+message_restaurant,
                    'Charset': 'UTF-8'
                }
            }
        }
    )


def lambda_handler(event, context):
    print(event)
    Cuisine = event['Records'][0]['messageAttributes']['Cuisine']['stringValue']
    DiningDate = event['Records'][0]['messageAttributes']['DiningDate']['stringValue']
    PhoneNumber = event['Records'][0]['messageAttributes']['PhoneNumber']['stringValue']
    CountPeople = event['Records'][0]['messageAttributes']['CountPeople']['stringValue']
    DiningTime = event['Records'][0]['messageAttributes']['DiningTime']['stringValue']
    Location = event['Records'][0]['messageAttributes']['Location']['stringValue']
    EmailAddr = event['Records'][0]['messageAttributes']['EmailAddr']['stringValue']
    
    restaurant_id_List = get_restaurants_from_elastic_search(Cuisine)
    restaurant_details = get_restaurant_details_from_dynamo(restaurant_id_List)
    send_email_using_ses(restaurant_details, EmailAddr, Cuisine, Location)

    return {
        'statusCode': 200,
        'body': json.dumps("LF2 running succesfully")
    }
