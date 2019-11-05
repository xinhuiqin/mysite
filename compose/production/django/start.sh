#!/bin/sh
python3 manage.py collectstatic --noinput
python manage.py makemigrations
python3 manage.py migrate
gunicorn mysite.wsgi:application -w 4 -k gthread -b 0.0.0.0:8000 --chdir=/app
