#!/bin/sh

echo "Waiting for PostgreSQL to start..."

while ! nc -z postgres 5432; do
  sleep 0.1
done

echo "PostgreSQL started"

gunicorn -b 0.0.0.0:5000 manage:app