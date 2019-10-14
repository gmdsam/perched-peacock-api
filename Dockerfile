FROM python:latest

RUN mkdir /app
WORKDIR /app

COPY . /app

ENV PYTHONPATH /app

RUN pip install -r requirements.txt

CMD python /app/parking/api/main.py