FROM python:3.9-slim-bullseye

WORKDIR app

COPY requirements.txt service/ ./

RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3", "api.py"]
