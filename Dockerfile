FROM python:3.8.0-slim as builder

WORKDIR /app

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt .

RUN apt-get update \
    && apt-get install gcc python-dev libpq-dev postgresql-client -y \
    && apt-get update -y && apt-get upgrade -y && apt-get install -y --no-install-recommends binutils libproj-dev gdal-bin libgdal-dev python3-gdal \
    && apt-get clean

RUN pip install --upgrade pip \
    && pip install -r requirements.txt

COPY . .

COPY ./build.sh .

RUN chmod +x /build.sh

CMD ["/build.sh"]
