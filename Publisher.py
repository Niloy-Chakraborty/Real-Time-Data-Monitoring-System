#!/usr/bin/env python
"""
Script Name: Publisher
Functionality: This script publish the json data to RabbitMQ
Author: Niloy Chakraborty
"""


# import dependencies
import pika
import time

"""
Function Name: publisher
Parameters: user_id, password,data,j,timestamp
Functionality: --This function takes json data from main
               -- Establish connection for the message queue
               -- publish the data into queue
               -- Goes to sleep for 10 secs
               -- closes the connection
Return: 
"""
def publisher(user_id, password,data,j,timestamp):

    credentials = pika.PlainCredentials(user_id, password)
    parameters = pika.ConnectionParameters('127.0.0.1', 5672, '/', credentials)
    connection = pika.BlockingConnection(parameters)

    channel = connection.channel()

    channel.queue_declare(queue='datacenter')
    #count = 0
    channel.basic_publish(exchange='',
                          routing_key='datacenter',
                          body=data  # "body",
                          )
    print(" [x] Sent 'publisher data' for node:" +j+ " of "+ timestamp)
    time.sleep(10)

    connection.close()


#publisher("guest","guest")


