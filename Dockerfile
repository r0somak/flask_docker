FROM ubuntu:18.04
LABEL maintainer="mikolaj.akartel@pollub.edu.pl"
RUN apt update && apt -y upgrade
RUN apt -y install python3 python3-pip virtualenv
RUN mkdir /app
WORKDIR /app
VOLUME /app
COPY ./startup.sh /app
RUN chmod +x /app/startup.sh
COPY ./requirements.txt /app
COPY ./wsgi.py /app
COPY ./application /app/application
EXPOSE 5000
CMD ["/app/startup.sh"]