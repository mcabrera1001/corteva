FROM python:3.10-slim

ENV PYTHONUNBUFFERED True

WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY . .
ENV FLASK_APP views/app.py
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]