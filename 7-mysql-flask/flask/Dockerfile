FROM python:3

RUN apt-get update -y && apt-get install -y \
    python3-pip \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip install -U pip

WORKDIR /app/

RUN pip3 install Flask \
    requests \
    flask-mysqldb 

COPY ./flask/app.py .

EXPOSE 5003

CMD [ "python","app.py" ]