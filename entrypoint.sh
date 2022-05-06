#!/bin/sh

python manage.py migrate
python manage.py collectstatic --no-input

gunicorn WattTime.wsgi:application --bind 0.0.0.0:8000 --timeout 300 --workers=3