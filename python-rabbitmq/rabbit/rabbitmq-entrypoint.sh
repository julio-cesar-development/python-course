#!/bin/bash

/rabbitmq-config.sh &
wait

# the parameter default to receive here in "$@" will be "rabbitmq-server" passed in Dockerfile
/usr/local/bin/docker-entrypoint.sh "$@"
