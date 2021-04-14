FROM python:3

WORKDIR /

COPY . .

RUN apt-get upgrade

EXPOSE 5000

CMD ["python3", "./app.py"]
