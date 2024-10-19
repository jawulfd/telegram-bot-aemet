FROM --platform=linux/arm64 python:3.11-slim-bullseye

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY src/ .

ENV PYTHONPATH /usr/src/app

CMD [ "python", "main.py" ]
