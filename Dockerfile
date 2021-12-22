FROM python:3.8-slim-buster

WORKDIR /var/rgb

ENV PYTHONPATH="${PYTHONPATH}:/var/rgb"

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

ENV FLASK_APP="/var/rgb/main.py"

CMD flask run --host=0.0.0.0
