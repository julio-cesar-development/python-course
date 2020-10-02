import pika
import os
import time
from random import randrange
import logging

rabbit_host = os.environ.get('RABBIT_HOST', 'localhost')
rabbit_port = os.environ.get('RABBIT_PORT', 5672)
rabbit_user = os.environ.get('RABBIT_USER', 'dev')
rabbit_pass = os.environ.get('RABBIT_PASS', 'dev')
rabbit_vhost = os.environ.get('RABBIT_VHOST', '/')

rabbit_queue = os.environ.get('RABBIT_QUEUE', 'event_queue_01')

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

logging.basicConfig(format="%(asctime)s - %(message)s", level=logging.INFO)

channel = connection.channel()
logging.info(channel)

def callback_queue(__channel, __method, __properties, __body):
  logging.info(__body)
  time.sleep(randrange(2, 6))

  # random logic to acknowledge or not
  acknowledge=randrange(0, 2) == 1
  if acknowledge:
    logging.info("WILL ACKNOWLEDGE")
    __channel.basic_ack(delivery_tag=__method.delivery_tag)
  else:
    logging.info("WILL NEGATIVELY ACKNOWLEDGE")
    __channel.basic_nack(delivery_tag=__method.delivery_tag)

  logging.info(" [x] Done")

# dont give more than one message to a worker at a time
channel.basic_qos(prefetch_count=1)

channel.basic_consume(
    queue=rabbit_queue, auto_ack=False, on_message_callback=callback_queue
)

logging.info(" [*] Waiting for messages on queue %s" % (rabbit_queue))
channel.start_consuming()
