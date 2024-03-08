FROM python:3.8-slim

WORKDIR /app

COPY . /app

RUN pip install flask requests

EXPOSE 5000

ENV FLASK_APP=app/main.py

CMD ["flask", "run", "--host=0.0.0.0"]