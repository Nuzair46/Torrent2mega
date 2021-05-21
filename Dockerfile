FROM ubuntu:latest

WORKDIR /app

#installing python,pip and gcc
RUN apt-get update
RUN apt-get install -y python3-pip python3-libtorrent

#installing reqs
COPY requirements.txt /app/requirements.txt
RUN pip3 install -r requirements.txt

#running the code
COPY driver.py /app/driver.py
CMD python3 driver.py