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

# rabbitmqctl set_policy TTL ".*" '{"message-ttl": 60000}' --apply-to queues

# queues
# rabbitmqadmin -u {user} -p {password} -V {vhost} declare queue name={nanme} auto_delete=false durable=true
rabbitmqadmin declare --vhost=/ queue name=event_queue_01 auto_delete=false durable=true arguments='{"x-message-ttl": 60000, "x-dead-letter-exchange":"dead_letter_exchange","x-dead-letter-routing-key":"dead_letter.#"}'
rabbitmqadmin declare --vhost=/ queue name=event_queue_02 auto_delete=false durable=true arguments='{"x-message-ttl": 60000, "x-dead-letter-exchange":"dead_letter_exchange","x-dead-letter-routing-key":"dead_letter.#"}'
# dead letter queue (TTL of 60 seconds)
rabbitmqadmin declare --vhost=/ queue name=dead_letter auto_delete=false durable=true

# exchanges
# types: direct, topic, headers and fanout
rabbitmqadmin declare exchange name=event_queue_exchange type=topic auto_delete=false durable=true
rabbitmqadmin declare exchange name=dead_letter_exchange type=direct auto_delete=false durable=true

# bindings
rabbitmqadmin declare binding source=event_queue_exchange destination=event_queue_01 routing_key="event_queue_01.#" destination_type=queue
rabbitmqadmin declare binding source=event_queue_exchange destination=event_queue_02 routing_key="event_queue_02.#" destination_type=queue
# dead letter binding
rabbitmqadmin declare binding source=dead_letter_exchange destination=dead_letter routing_key="dead_letter.#" destination_type=queue
