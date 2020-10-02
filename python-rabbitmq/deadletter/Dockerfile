FROM python:3.5-alpine
LABEL maintainer="Julio Cesar <julio@blackdevs.com.br>"

WORKDIR /app
RUN pip install pika==1.1.0

COPY . .

CMD [ "python", "-u", "main.py" ]

# build the image
# docker image build --tag deadletter:latest ./deadletter

# run container in regular mode
# docker container run --rm -v ${PWD}:/deadletter/ --name deadletter deadletter:latest

# run  in interactive mode and replacing entrypoint to access sh
# docker container run --rm -v ${PWD}:/deadletter/ -it --entrypoint "" deadletter:latest /bin/sh

# build and push
# docker image build --tag juliocesarmidia/app-deadletter:v1.0.0 ./deadletter
# docker image push juliocesarmidia/app-deadletter:v1.0.0
