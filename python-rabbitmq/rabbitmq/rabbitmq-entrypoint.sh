#!/bin/bash

/rabbitmq-config.sh &

/usr/local/bin/docker-entrypoint.sh "$@"
