#!/usr/bin/env bash

set -e

bash /scrapy-bench/start-servers.sh

cd center
uwsgi \
    --module=center.wsgi:application \
    --env DJANGO_SETTINGS_MODULE=center.settings \
    --env DEBUG=0 \
    --static-map /static=./center/sitestatic \
    --master \
    --http=0.0.0.0:8000 \
    --processes=2 \
    --threads=4
