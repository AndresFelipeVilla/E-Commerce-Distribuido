FROM python:3.10-slim
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN python -m pip install --upgrade pip 
RUN python -m pip install --no-cache-dir -r /app/requirements.txt

COPY ./inventory /app/