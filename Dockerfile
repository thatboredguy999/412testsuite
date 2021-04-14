FROM python:3

WORKDIR /

COPY . .

RUN apt-get upgrade
RUN python3
RUN md5test()

EXPOSE 5000

CMD ["python3", "./app.py"]
