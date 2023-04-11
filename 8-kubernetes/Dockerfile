FROM python:3

RUN apt-get update -y && apt-get install -y \
    python3-pip \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

RUN pip install -U pip

RUN pip3 install Flask

COPY . .

EXPOSE 5008

CMD ["python", "project/app.py"]