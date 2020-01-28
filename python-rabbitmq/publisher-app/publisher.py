#!/usr/bin/env python
import pika
import os
import json
import sys
import time

rabbit_host = os.environ.get('RABBIT_HOST', 'localhost')
rabbit_port = os.environ.get('RABBIT_PORT', 5672)
rabbit_user = os.environ.get('RABBIT_USER', 'dev')
rabbit_pass = os.environ.get('RABBIT_PASS', 'dev')
rabbit_vhost = os.environ.get('RABBIT_VHOST', '/')
rabbit_queue = os.environ.get('RABBIT_QUEUE', 'event_queue')
rabbit_routing_key = os.environ.get('RABBIT_ROUTING_KEY', 'event_queue')
rabbit_exchange = os.environ.get('RABBIT_EXCHANGE', 'event_queue_exchange')

time.sleep(20)

amqp_credentials = pika.PlainCredentials(rabbit_user, rabbit_pass)
connection = pika.BlockingConnection(
  pika.ConnectionParameters(
    host=rabbit_host,
    port=rabbit_port,
    credentials=amqp_credentials,
    virtual_host=rabbit_vhost,
  )
)

channel = connection.channel()
print('channel', channel)

# result = channel.queue_declare(queue=rabbit_queue, durable=True)
# channel.exchange_declare(exchange=rabbit_exchange, exchange_type='fanout')
# channel.queue_bind(exchange=rabbit_exchange, queue=rabbit_queue)

message_id = ''.join(sys.argv[1:]) or 1
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

basic_publish(message, rabbit_routing_key)

def exchange_publish(__message, __exchange, __routing_key=''):
  # Here it will be sent to specified exchange
  channel.basic_publish(exchange=__exchange,
                        routing_key=__routing_key,
                        body=__message,
                        properties=pika.BasicProperties(
                          delivery_mode = 2, # persistent message, also que queue needs to be durable=True
                        ))

print(" [x] Sent message :: %r" % (message))
connection.close()
