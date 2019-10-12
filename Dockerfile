FROM python:latest

RUN mkdir /app
WORKDIR /app

COPY . /app

ENV PYTHONPATH /app/pp-parking

RUN pip install -r requirements.txt

CMD python /app/pp-parking/parking/api/main.py