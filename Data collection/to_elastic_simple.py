import json
import boto3
import datetime
from botocore.vendored import requests
from elasticsearch import Elasticsearch, RequestsHttpConnection
import csv
from io import BytesIO

host = 'search-diningconciergeold-y36aixk37hngct542nd7rrtojm.us-west-2.es.amazonaws.com'

es = Elasticsearch(
    hosts = [{'host': host, 'port': 443}],
    use_ssl = True,
    verify_certs = True,
    connection_class = RequestsHttpConnection
)
print(es)
with open('Yelp_Restaurants.csv', newline='') as f:
    reader = csv.reader(f)
    restaurants = list(reader)

for restaurant in restaurants:
    index_data = {
        'id': restaurant[0],
        'categories': restaurant[2]
    }
    print ('dataObject', index_data)

    es.index(index="restaurants", doc_type="Restaurant", id=restaurant[0], body=index_data, refresh=True)