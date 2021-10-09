# Dining-Concierge-Chatbot

## An AWS based Dining Concierge Chatbot designed in the fulfillment of Assignment 1 of CS-GY 9223-I Cloud Computing and Big Data Systems
***

## Contributers: 
#### NIKHIL KISHAN KHANEJA (nkk6190) | RAJAT RAGHUVANSHI (rrr****)

***

## DESCRIPTION:

#### Customer Service is a core service for a lot of businesses around the world and it is getting disrupted at the moment by Natural Language Processing-powered applications. In this assignmet we have implemented a serverless, microservice-driven web-based Dining Concierge chatbot that sends you restaurant suggestions given a set of preferences that you provide the chatbot with through conversation.

#### So based on a conversation with the customer, the LEX chatbot will identify the customer’s preferred ‘cuisine’. The chatbot will search through ElasticSearch to get random suggestions of restaurant IDs with this cuisine. The chatbot will also query the DynamoDB table with these restaurant IDs to find more information about the restaurants you want to suggest to your customers like name and address of the restaurant. The chatbot will filter the restaurants based on the Cuisine.

***

## SERVICES USED

### AWS SERVICES 
#### ▫️ AWS S3 BUCKET: 
Amazon Simple Storage Service (Amazon S3) is an object storage service that offers industry-leading scalability, data availability, security, and performance. Object storage service that offers industry-leading scalability, data availability, security, and performance.

#### ▫️ AWS LEX: 
Amazon Lex is a fully managed artificial intelligence (AI) service with advanced natural language models for building conversational interfaces into applications such as _Build virtual agents and voice assistants_ ,_Automate informational responses_ ,and _Improve productivity with application bots_. 

#### ▫️ AWS LAMBDA : 
AWS Lambda is a serverless compute service that lets you run code without provisioning or managing servers, creating workload-aware cluster scaling logic, maintaining event integrations, or managing runtimes. With Lambda, we ran code for the application with zero administration. 

#### ▫️ AWS API GATEWAY: 
Amazon API Gateway is a fully managed service that makes it easy for developers to create, publish, maintain, monitor, and secure APIs at any scale. APIs act as the "front door" for applications to access data, business logic, or functionality from your backend services. Using API Gateway, we were able to create RESTful APIs that enable real-time two-way communication applications. API Gateway supports containerized and serverless workloads, as well as web applications.

#### ▫️ AWS SIMPLE QUEUE SERVICE (SQS):
Amazon Simple Queue Service (SQS) is a fully managed message queuing service that enables you to decouple and scale microservices, distributed systems, and serverless applications. SQS eliminates the complexity and overhead associated with managing and operating message-oriented middleware, and empowers developers to focus on differentiating work. Using SQS, you can send, store, and receive messages between software components at any volume, without losing messages or requiring other services to be available. We used Standard message queue for best throughput, best-effort ordering, and at-least-once delivery

#### ▫️ AWS SIMPLE QUEUE SERVICE (SQS): 
Amazon Simple Queue Service (SQS) is a fully managed message queuing service that enables you to decouple and scale microservices, distributed systems, and serverless applications. SQS eliminates the complexity and overhead associated with managing and operating message-oriented middleware, and empowers developers to focus on differentiating work. Using SQS, you can send, store, and receive messages between software components at any volume, without losing messages or requiring other services to be available. We used Standard message queue for best throughput, best-effort ordering, and at-least-once delivery.

#### ▫️ AWS SIMPLE NOTIFICATION SERVICE (SNS): 
Amazon Simple Notification Service (Amazon SNS) is a fully managed messaging service for both application-to-application (A2A) and application-to-person (A2P) communication. We have used AWS SNS to push the recommendations to the user. The A2P functionality enables you to send messages to users at scale via SMS, mobile push, and email. We have used email and SMS notifications.

#### ▫️ AWS Elasticsearch : 
AWS Elasticsearch is a distributed search and analytics engine built on Apache Lucene. Since its release in 2010, Elasticsearch has quickly become the most popular search engine and is commonly used for log analytics, full-text search, security intelligence, business analytics, and operational intelligence use cases.

#### ▫️ AWS DynamoDB:
Amazon DynamoDB is a fully managed, serverless, key-value NoSQL database designed to run high-performance applications at any scale. DynamoDB offers built-in security, continuous backups, automated multi-region replication, in-memory caching, and data export tools. It is used to design _Develop software applications_, _Create media metadata stores_, and _Deliver seamless retail experiences_

### YELP API SERVICES 
The Yelp Fusion API allows you to get the best local content and user reviews from millions of businesses across 32 countries. This tutorial provides an overview of the capabilities our suite of APIs offer, provides instructions for how to authenticate API calls, and walks through a simple scenario using the API.

#### ▫️ YELP AUTHENTICATION:
The Yelp Fusion API uses private key authentication to authenticate all endpoints. Your private API Key will be automatically generated after you create your app. 

***

## WORKFLOW DIAGRAM 
![alt text](https://github.com/rajat10cube/Dining-Concierge-using-AWS/blob/main/images/Assignment%201%20architecture%20diagram.png)

***

##SAMPLE USE CASE

*User*: Hello

*Bot*: Hi there, how can I help?
*User*: I need some restaurant suggestions.
*Bot*: Great. I can help you with that. What city or city area are you looking to dine in?
*User*: Manhattan
*Bot*: Got it, Manhattan. What cuisine would you like to try?
*User*: Chinese
*Bot*: Ok, how many people are in your party?
*User*: 4
*Bot*: A few more to go. What date?
*User*: Today
*Bot*: What time?
*User*: 1 pm
*Bot*: Great. Lastly, I need your phone number so I can send you my findings.
*User*: 9879876655
*Bot*: You’re all set. Expect my suggestions shortly! Have a good day.
*User*: Thank you!
Bot: You’re welcome.
