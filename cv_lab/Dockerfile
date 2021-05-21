FROM python:3.9.5-buster

WORKDIR /lab

RUN apt-get update &&\
    apt-get install ffmpeg libsm6 libxext6  -y

COPY requirements.txt /lab

RUN pip install -r /lab/requirements.txt

COPY . /lab/

ENTRYPOINT ["tail", "-f", "/dev/null"]