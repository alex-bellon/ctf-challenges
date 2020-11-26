FROM ubuntu:16.04

RUN apt-get update
RUN apt-get update && apt-get install -y build-essential socat libseccomp-dev
RUN apt-get install -y python3

ARG USER
ENV USER $USER

COPY ./start.sh /start.sh
COPY ./run.py /run.py
COPY ./valid.txt /valid.txt
COPY ./invalid.txt /invalid.txt

RUN useradd -m $USER

RUN chmod 755 /start.sh

EXPOSE 9000

CMD ["/start.sh"]
