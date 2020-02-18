#!/bin/bash

while true; do
  sleep 5
  rabbitmqctl -q node_health_check > /dev/null 2>&1

  test $? == 0 && break
done

rabbitmqctl add_user dev dev
rabbitmqctl set_user_tags dev administrator
rabbitmqctl set_permissions -p / dev ".*" ".*" ".*"

rabbitmqctl set_permissions -p / guest ".*" ".*" ".*"

# amqp tools
# apt-get install amqp-tools -y

# ### basic config
# # queues
# rabbitmqadmin declare --vhost=/ queue name=event_queue auto_delete=false durable=true

# # exchanges
# # types: direct, topic, headers and fanout
# rabbitmqadmin declare exchange name=default type=fanout auto_delete=false durable=true

# # bindings
# rabbitmqadmin declare binding source=default destination=event_queue destination_type=queue

### advanced config
# queues
# rabbitmqadmin -u {user} -p {password} -V {vhost} declare queue name={nanme} auto_delete=false durable=true
rabbitmqadmin declare --vhost=/ queue name=event_queue_01 auto_delete=false durable=true
rabbitmqadmin declare --vhost=/ queue name=event_queue_02 auto_delete=false durable=true

# exchanges
# types: direct, topic, headers and fanout
# fanout exchange: it broadcasts all the messages it receives to all the queues it knows
rabbitmqadmin declare exchange name=event_queue_exchange type=fanout auto_delete=false durable=true

# bindings
rabbitmqadmin declare binding source=event_queue_exchange destination=event_queue_01 routing_key="event_queue_01.#" destination_type=queue
rabbitmqadmin declare binding source=event_queue_exchange destination=event_queue_02 routing_key="event_queue_02.#" destination_type=queue
