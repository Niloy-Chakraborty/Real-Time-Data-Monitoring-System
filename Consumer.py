#!/usr/bin/env python
"""
Script Name: Consumer
Functionality: This script consumes the json data from RabbitMQ
Author: Niloy Chakraborty
"""

# import dependencies
import pika
import influxConnect
import simplejson as json
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='datacenter')

"""
Function Name: callback
Parameters: ch, method, properties, body
Functionality: -- Connects to the channel
               --Consumes the data that is already in the Message Queue
                
Return: 
"""


def callback(ch, method, properties, body):
    # body= json.loads(body)
    # data= body.decode()
    # print(body)
    my_json = body.decode('utf8')
    # print(my_json)
    print(my_json)

    # Call for InfluxDB to insert the data
    influxConnect.push_data(my_json)


channel.basic_consume(queue='datacenter', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()