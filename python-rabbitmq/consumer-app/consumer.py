#!/usr/bin/env python
import pika
import os
import json
import time
from random import randrange

rabbit_host = os.environ.get('RABBIT_HOST', 'localhost')
rabbit_queue = os.environ.get('RABBIT_QUEUE', 'event_queue')
rabbit_routing_key = os.environ.get('RABBIT_ROUTING_KEY', 'event_queue')
rabbit_exchange = os.environ.get('RABBIT_EXCHANGE', 'event_queue_exchange')

connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbit_host))
channel = connection.channel()

# result = channel.queue_declare(queue=rabbit_queue, durable=True)
# channel.exchange_declare(exchange=rabbit_exchange, exchange_type='fanout')
# channel.queue_bind(exchange=rabbit_exchange, queue=rabbit_queue)

def callback(ch, method, properties, body):
  print(" [x] Received :: %r" % body)
  time.sleep(randrange(2, 5))
  print(" [x] Done")
  ch.basic_ack(delivery_tag = method.delivery_tag)

# not give more than one message to a worker at a time
channel.basic_qos(prefetch_count=1)

def consume(__queue, __callback):
  channel.basic_consume(queue=__queue,
                        on_message_callback=__callback)

consume(rabbit_queue, callback)

print(' [*] Waiting for messages')
channel.start_consuming()
