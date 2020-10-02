import pika
import os
import json
import sys
import time
import logging
from random import randrange

rabbit_host = os.environ.get('RABBIT_HOST', 'localhost')
rabbit_port = os.environ.get('RABBIT_PORT', 5672)
rabbit_user = os.environ.get('RABBIT_USER', 'dev')
rabbit_pass = os.environ.get('RABBIT_PASS', 'dev')
rabbit_vhost = os.environ.get('RABBIT_VHOST', '/')
rabbit_exchange = os.environ.get('RABBIT_EXCHANGE', 'event_queue_exchange')

amqp_credentials = pika.PlainCredentials(rabbit_user, rabbit_pass)

connection = pika.BlockingConnection(
  pika.ConnectionParameters(
    host=rabbit_host,
    port=rabbit_port,
    credentials=amqp_credentials,
    virtual_host=rabbit_vhost,
    heartbeat=0,
  )
)

channel = connection.channel()
logging.info(channel)

message_id = ''.join(sys.argv[1:]) or int(randrange(1000, 10001))
message = json.dumps({ 'id': message_id, 'data': { 'payload': 'RABBIT' } })

def basic_publish(__message, __routing_key):
  # With an empty exchange it will end up using the default exchange,
  # and thus it will be sent to queue with name specified in routing_key
  channel.basic_publish(exchange='',
                        routing_key=__routing_key,
                        body=__message,
                        properties=pika.BasicProperties(
                          delivery_mode = 2, # persistent message, also que queue needs to be durable=True
                        ))

# basic_publish(message, 'event_queue')

def exchange_publish(__message, __exchange, __routing_key=''):
  # Here it will be sent to specified exchange
  channel.basic_publish(exchange=__exchange,
                        routing_key=__routing_key,
                        body=__message,
                        properties=pika.BasicProperties(
                          delivery_mode = 2, # persistent message, also que queue needs to be durable=True
                        ))

# publish to exchange with 2 different routing keys
exchange_publish(message, rabbit_exchange, 'event_queue_01.event')
exchange_publish(message, rabbit_exchange, 'event_queue_02.event')

logging.info(" [x] Sent message :: %r" % (message))
connection.close()

sys.exit(0)
