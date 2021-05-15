FROM ubuntu:18.04

RUN apt-get update
RUN apt-get update && apt-get install -y build-essential socat libseccomp-dev
RUN apt-get update && apt-get install -y python3.8 python3-pip
RUN pip3 install numpy

ARG USER
ENV USER $USER

COPY ./start.sh /start.sh
COPY ./ev.py /ev.py

RUN useradd -m $USER

RUN chmod 755 /start.sh

EXPOSE 9000

CMD ["/start.sh"]
