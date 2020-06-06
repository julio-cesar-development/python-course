FROM python:3.5-alpine
LABEL maintainer="Julio Cesar <julio@blackdevs.com.br>"

WORKDIR /app
COPY ./ /app

RUN pip install pika==1.1.0
RUN chmod +x /app/main.py

CMD [ "/usr/local/bin/python", "/app/main.py" ]

# build the image
# docker image build --tag dead_letter -f Dockerfile ./dead-letter

# run container in regular mode
# docker container run --rm -v ${PWD}:/dead-letter/ --name dead_letter dead_letter

# run  in interactive mode and replacing entrypoint to access sh
# docker container run --rm -v ${PWD}:/dead-letter/ -it --entrypoint "" dead_letter /bin/sh
