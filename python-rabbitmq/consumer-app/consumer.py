#!/usr/bin/env python
import pika
import os
import json
import time
from random import randrange

rabbit_host = os.environ.get('RABBIT_HOST', 'localhost')
rabbit_port = os.environ.get('RABBIT_PORT', 5672)
rabbit_user = os.environ.get('RABBIT_USER', 'dev')
rabbit_pass = os.environ.get('RABBIT_PASS', 'dev')
rabbit_vhost = os.environ.get('RABBIT_VHOST', '/')

rabbit_queue = os.environ.get('RABBIT_QUEUE', 'invalid')

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

def callback_queue(channel, method, properties, body):
  print(body)
  time.sleep(randrange(2, 5))
  print(" [x] Done")
  channel.basic_ack(delivery_tag=method.delivery_tag)

# dont give more than one message to a worker at a time
channel.basic_qos(prefetch_count=10)

channel.basic_consume(queue=rabbit_queue, auto_ack=False, on_message_callback=callback_queue)

print(' [*] Waiting for messages')
channel.start_consuming()
