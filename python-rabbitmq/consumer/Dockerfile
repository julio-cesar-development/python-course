FROM python:3.5-alpine
LABEL maintainer="Julio Cesar <julio@blackdevs.com.br>"

WORKDIR /app
RUN pip install pika==1.1.0

COPY . .

CMD [ "python", "-u", "consumer.py" ]

# build the image
# docker image build --tag consumer:latest ./consumer

# run container in regular mode
# docker container run --rm -v ${PWD}:/consumer/ --name consumer consumer:latest

# run  in interactive mode and replacing entrypoint to access sh
# docker container run --rm -v ${PWD}:/consumer/ -it --entrypoint "" consumer:latest /bin/sh

# build and push
# docker image build --tag juliocesarmidia/app-consumer:v1.0.0 ./consumer
# docker image push juliocesarmidia/app-consumer:v1.0.0
