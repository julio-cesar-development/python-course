FROM python:3.5-alpine
LABEL maintainer="Julio Cesar <julio@blackdevs.com.br>"

WORKDIR /app
RUN pip install pika==1.1.0

COPY . .

CMD [ "python", "-u", "publisher.py" ]

# build the image
# docker image build --tag publisher:latest ./publisher

# run container in regular mode
# docker container run --rm -v ${PWD}:/publisher/ --name publisher publisher:latest

# run  in interactive mode and replacing entrypoint to access sh
# docker container run --rm -v ${PWD}:/publisher/ -it --entrypoint "" publisher:latest /bin/sh
