FROM python:3.10-alpine

ENV PYTHONUNBUFFERED=1

COPY requirements.txt /requirements.txt
RUN apk add --update --no-cache --virtual .tmp gcc libc-dev linux-headers && \
    apk add --no-cache mariadb-connector-c-dev && \
    pip install -r /requirements.txt && \
    apk del .tmp

COPY ./app /app
WORKDIR /app

RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static

RUN adduser --disabled-password --no-create-home inacapi
RUN chown -R inacapi:inacapi /vol
RUN chown -R inacapi:inacapi /app
RUN chmod -R 755 /vol/web
USER inacapi

CMD ["uwsgi", "--socket", ":8000", "--workers", "4", "--master", "--enable-threads", "--module", "web.wsgi"]
