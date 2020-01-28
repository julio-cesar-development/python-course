FROM rabbitmq:3.7-management
LABEL maintainer="Julio Cesar <julio@blackdevs.com.br>"

RUN apt-get update && apt-get install -y wget unzip netcat supervisor && rm -rf /var/lib/apt/lists/*

ARG RABBITMQ_DME_VERSION="3.7.x"

RUN wget https://dl.bintray.com/rabbitmq/community-plugins/${RABBITMQ_DME_VERSION}/rabbitmq_delayed_message_exchange/rabbitmq_delayed_message_exchange-20171201-${RABBITMQ_DME_VERSION}.zip
RUN unzip rabbitmq_delayed_message_exchange-20171201-${RABBITMQ_DME_VERSION}.zip -d /plugins
RUN rabbitmq-plugins enable --offline rabbitmq_delayed_message_exchange
RUN rm rabbitmq_delayed_message_exchange-20171201-${RABBITMQ_DME_VERSION}.zip

COPY rabbitmq-config.sh /rabbitmq-config.sh
COPY rabbitmq-entrypoint.sh /rabbitmq-entrypoint.sh

RUN chmod +x /rabbitmq-config.sh /rabbitmq-entrypoint.sh

ENTRYPOINT ["sh", "/rabbitmq-entrypoint.sh"]

HEALTHCHECK --interval=5s --timeout=5s --start-period=5s --retries=3 CMD [ "rabbitmqctl", "-q", "node_health_check" ]

CMD "rabbitmq-server"
