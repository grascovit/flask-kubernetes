FROM python:3.8.2-alpine3.11

WORKDIR /usr/src/app

COPY ./requirements.txt /usr/src/app/requirements.txt

RUN apk add --no-cache --virtual .build-deps libffi-dev gcc musl-dev postgresql-dev

RUN pip install -r requirements.txt

COPY ./entrypoint.sh /usr/src/app/entrypoint.sh
RUN chmod +x /usr/src/app/entrypoint.sh

COPY . /usr/src/app

CMD ["/usr/src/app/entrypoint.sh"]