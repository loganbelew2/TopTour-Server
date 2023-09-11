#!/bin/bash

rm db.sqlite3
rm -rf ./toptourapi/migrations
python3 manage.py migrate
python3 manage.py makemigrations toptourapi
python3 manage.py migrate toptourapi
python3 manage.py loaddata users
python3 manage.py loaddata tokens
python3 manage.py loaddata tourists
python3 manage.py loaddata attractions
python3 manage.py loaddata categories
python3 manage.py loaddata posts
python3 manage.py loaddata comments
