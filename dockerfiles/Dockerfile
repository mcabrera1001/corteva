FROM python:3.10-slim

ENV PYTHONUNBUFFERED True

WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY . .
ENV FLASK_APP endpoints/app.py
CMD [ "flask", "run"]