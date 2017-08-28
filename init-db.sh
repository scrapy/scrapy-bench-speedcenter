#!/usr/bin/env bash
set -e

cd center

python2.7 manage.py migrate
python2.7 center/gen-initial-data.py \
    "CPython 2.7.13,CPython 3.5.4,CPython 3.6.2" \
    "1.1.0,1.2.0,1.3.0,1.4.0,master" \
    > center/initial-data.json
python2.7 manage.py loaddata center/initial-data.json
