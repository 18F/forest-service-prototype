#!/bin/sh
bash wait-for-it.sh -s -q -t 0 db:5432 
python manage.py migrate
python manage.py runserver 0.0.0.0:$PORT
