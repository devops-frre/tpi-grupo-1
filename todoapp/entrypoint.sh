#!/bin/sh

# Ensure that Postgres is healthy
if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

python manage.py migrate
# Remover ->
python manage.py collectstatic --no-input --clear

# Launch the web server
exec "$@"