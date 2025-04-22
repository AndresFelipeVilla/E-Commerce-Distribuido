FROM python:3.10-slim
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN apt-get update && apt-get install -y libpq-dev gcc python3-dev \
    && rm -rf /var/lib/apt/lists/*

RUN python -m pip install --upgrade pip 
RUN python -m pip install --no-cache-dir -r requirements.txt

COPY ./producto /app/