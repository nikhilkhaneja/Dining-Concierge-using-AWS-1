import requests
import csv
import time
import boto3
import pandas as pd
import os
from datetime import datetime
from decimal import Decimal

# upload to DynamoDB
AWS_DB_REGION = 'us-west-2'
AWS_TABLE_NAME = 'yelp-restaurants'
AWS_PRIMARY_KEY = 'RestaurantID'
CSV_FILE = 'Yelp_Restaurants.csv'
CSV_HEAD = [AWS_PRIMARY_KEY, 'Name', 'Cuisine', 'Rating', 'TotalReviews',
            'Address', 'ZipCode', 'Latitude', 'Longitude', 'IsClosed',
            'TimeStamp']


YELP_REQ_CUISINES = ['italian', 'chinese', 'mexican', 'american',
                     'korean', 'thai', 'arab', 'Caribbean'
                     'vietnamese', 'indian']

def uploadToDynamoDB():
    print ('=========== start uploading data to DynamoDB ===========')
    # init csv file and AWS
    yelp_csv = pd.read_csv(CSV_FILE)
    dynamodb = boto3.resource('dynamodb', region_name=AWS_DB_REGION)
    table = dynamodb.Table(AWS_TABLE_NAME)

    # init counting var
    cuisine_last = str(yelp_csv[CSV_HEAD[2]][0])
    cuisine_type = 1
    cuisine_count = 0
    total_count = 0
    start_time = time.time()
    point_time = start_time

    # upload
    for i in range(len(yelp_csv)):
        cuisine_curr = str(yelp_csv[CSV_HEAD[2]][i])
        cuisine_count += 1
        total_count += 1
        item = {CSV_HEAD[0]: str(yelp_csv[CSV_HEAD[0]][i]),
                CSV_HEAD[1]: str(yelp_csv[CSV_HEAD[1]][i]),
                CSV_HEAD[2]: str(yelp_csv[CSV_HEAD[2]][i]),
                CSV_HEAD[3]: Decimal(yelp_csv[CSV_HEAD[3]][i].astype(Decimal)),
                CSV_HEAD[4]: Decimal(yelp_csv[CSV_HEAD[4]][i].astype(Decimal)),
                CSV_HEAD[5]: str(yelp_csv[CSV_HEAD[5]][i]),
                CSV_HEAD[6]: str(yelp_csv[CSV_HEAD[6]][i]),
                CSV_HEAD[7]: str(yelp_csv[CSV_HEAD[7]][i]),
                CSV_HEAD[8]: str(yelp_csv[CSV_HEAD[8]][i]),
                CSV_HEAD[9]: str(yelp_csv[CSV_HEAD[9]][i].astype(str)),
                CSV_HEAD[10]: str(yelp_csv[CSV_HEAD[10]][i])}
        table.put_item(Item=item)

        # finish uploading a cuisine type
        if cuisine_curr != cuisine_last:
            now = time.time()
            print ('(%d/%d) cuisine: "%s" uploaded, time spent: %ds, total time: %ds, current item: %d, total item: %d' % (
                cuisine_type, len(YELP_REQ_CUISINES), cuisine_last,
                int(now - point_time), int(now - start_time),
                cuisine_count, total_count))
            point_time = now
            cuisine_last = cuisine_curr
            cuisine_count = 0
            cuisine_type += 1

    # finish uploading last cuisine type
    print ('(%d/%d) cuisine: "%s" uploaded, time spent: %ds, total time: %ds, current item: %d, total item: %d' % (
        cuisine_type, len(YELP_REQ_CUISINES), cuisine_curr,
        int(now - point_time), int(now - start_time),
        cuisine_count, total_count))

    print ('=========== uploading data to DynamoDB done ===========')


uploadToDynamoDB()
