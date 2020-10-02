#!/bin/bash

/rabbitmq-config.sh &

# the parameter default to receive here in "$@" will be "rabbitmq-server" passed in Dockerfile
/usr/local/bin/docker-entrypoint.sh "$@"
