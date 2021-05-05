# syntax=docker/dockerfile:1

FROM ubuntu:latest

ENV TZ=Europe/Kiev
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get update -y
RUN apt-get install -y python3-pip python3-dev build-essential
RUN apt update && apt install -y libsm6 libxext6 libxrender-dev libgl1-mesa-dev
RUN apt-get -y install tesseract-ocr tesseract-ocr-ukr

COPY . /app

WORKDIR /app

RUN pip3 install -r requirements.txt

CMD ["python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=8080"]
