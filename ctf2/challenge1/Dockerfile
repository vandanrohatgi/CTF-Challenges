FROM python:3.6.9-alpine
COPY requirements.txt /
RUN pip3 install -r /requirements.txt
COPY ./app /app
WORKDIR /app
EXPOSE 8000
ENTRYPOINT ["./gunicorn_starter.sh"]
