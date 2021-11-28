FROM python:3.9-slim-bullseye

WORKDIR app

COPY requirements.txt wait-for-it.sh service/ ./

RUN pip3 install -r requirements.txt

ENTRYPOINT ["./wait-for-it.sh", "mysql:3306", "--", "python3", "api.py"]
