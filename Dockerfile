FROM ubuntu

COPY . /app
WORKDIR /app

RUN apt-get update
RUN apt-get install -y python3-pip
RUN pip3 install flask
RUN apt-get install -y nmap

ENTRYPOINT ["python3"]
CMD ["app.py"]
EXPOSE 80
