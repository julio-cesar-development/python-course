FROM python:3.5-alpine
LABEL maintainer="Julio Cesar <julio@blackdevs.com.br>"

WORKDIR /app
COPY ./publisher-app /app

RUN pip install pika
RUN chmod +x /app/publisher.py

ENTRYPOINT [ "python", "/app/publisher.py" ]

# build the image
# docker image build --tag publisher_app -f Dockerfile ./publisher-app

# run container in regular mode
# docker container run --rm -v ${PWD}:/publisher-app/ --name publisher_app publisher_app

# run  in interactive mode and replacing entrypoint to access sh
# docker container run --rm -v ${PWD}:/publisher-app/ -it --entrypoint "" publisher_app /bin/sh
