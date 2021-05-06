#!/bin/bash
virtualenv -p python3 venv
. ./venv/bin/activate
pip install -r requirements.txt
gunicorn --workers 2 --bind 0.0.0.0:5000 wsgi:flask_app