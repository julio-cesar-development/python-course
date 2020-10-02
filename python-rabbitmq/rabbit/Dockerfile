FROM rabbitmq:3.7-management
LABEL maintainer="Julio Cesar <julio@blackdevs.com.br>"

RUN apt-get update -yqq && \
    apt-get install -yqq \
    wget unzip netcat supervisor && \
    rm -rf /var/lib/apt/lists/*

ARG RABBITMQ_DME_VERSION="3.7.x"

RUN wget https://dl.bintray.com/rabbitmq/community-plugins/${RABBITMQ_DME_VERSION}/rabbitmq_delayed_message_exchange/rabbitmq_delayed_message_exchange-20171201-${RABBITMQ_DME_VERSION}.zip
RUN unzip rabbitmq_delayed_message_exchange-20171201-${RABBITMQ_DME_VERSION}.zip -d /plugins
RUN rabbitmq-plugins enable --offline rabbitmq_delayed_message_exchange
RUN rm rabbitmq_delayed_message_exchange-20171201-${RABBITMQ_DME_VERSION}.zip

COPY rabbitmq-config.sh /rabbitmq-config.sh
COPY rabbitmq-entrypoint.sh /rabbitmq-entrypoint.sh

RUN chmod +x /rabbitmq-config.sh /rabbitmq-entrypoint.sh

# it will call script rabbitmq-entrypoint.sh, passing the argument "rabbitmq-server" defined below in CMD
ENTRYPOINT ["sh", "/rabbitmq-entrypoint.sh"]

HEALTHCHECK --interval=5s --timeout=5s --start-period=10s --retries=3 CMD [ "rabbitmqctl", "-q", "node_health_check" ]

# it will be passed as argument complementing the entrypoint
CMD "rabbitmq-server"

# The first command to be executed will be: /bin/sh /rabbitmq-entrypoint.sh rabbitmq-server

# build and push
# docker image build --tag juliocesarmidia/app-rabbit:v1.0.0 ./rabbit
# docker image push juliocesarmidia/app-rabbit:v1.0.0
