FROM python:3.10

WORKDIR /app

COPY . /app

RUN pip install flask prometheus_client

EXPOSE 5000

CMD ["python", "app.py"]