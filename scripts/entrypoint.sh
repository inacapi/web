#!/bin/sh

set -e

python manage.py collectstatic --no-input
python manage.py migrate --no-input

uwsgi --socket :8000 --master --enable-threads --module web.wsgi