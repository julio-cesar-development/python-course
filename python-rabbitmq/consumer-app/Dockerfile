FROM python:3.5-alpine
LABEL maintainer="Julio Cesar <julio@blackdevs.com.br>"

WORKDIR /app
COPY ./ /app

RUN pip install pika==1.1.0
RUN chmod +x /app/consumer.py

ENTRYPOINT [ "python", "/app/consumer.py" ]

# build the image
# docker image build --tag consumer_app -f Dockerfile ./consumer-app

# run container in regular mode
# docker container run --rm -v ${PWD}:/consumer-app/ --name consumer_app consumer_app

# run  in interactive mode and replacing entrypoint to access sh
# docker container run --rm -v ${PWD}:/consumer-app/ -it --entrypoint "" consumer_app /bin/sh
