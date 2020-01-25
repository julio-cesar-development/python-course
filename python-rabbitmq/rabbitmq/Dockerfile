FROM rabbitmq:3.7-management
LABEL maintainer="Julio Cesar <julio@blackdevs.com.br>"

RUN apt-get update && apt-get install -y \
    unzip \
    netcat \
  && rm -rf /var/lib/apt/lists/*

ARG RABBIT_MESSAGE_EXCHANGE_VERSION="3.7.x"

ADD https://dl.bintray.com/rabbitmq/community-plugins/${RABBIT_MESSAGE_EXCHANGE_VERSION}/rabbitmq_delayed_message_exchange/rabbitmq_delayed_message_exchange-20171201-${RABBIT_MESSAGE_EXCHANGE_VERSION}.zip /tmp/rabbitmq_delayed_message_exchange-20171201-${RABBIT_MESSAGE_EXCHANGE_VERSION}.zip

RUN unzip /tmp/rabbitmq_delayed_message_exchange-20171201-${RABBIT_MESSAGE_EXCHANGE_VERSION}.zip -d /plugins
RUN rabbitmq-plugins enable --offline rabbitmq_delayed_message_exchange

COPY rabbitmq-config.sh /rabbitmq-config.sh
COPY rabbitmq-entrypoint.sh /rabbitmq-entrypoint.sh

RUN chmod +x /rabbitmq-config.sh /rabbitmq-entrypoint.sh

ENTRYPOINT ["sh", "/rabbitmq-entrypoint.sh"]

HEALTHCHECK --interval=5s --timeout=5s --start-period=5s --retries=3 CMD [ "rabbitmqctl", "-q", "node_health_check" ]

CMD "rabbitmq-server"
