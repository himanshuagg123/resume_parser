#!/usr/bin/env bash
echo "Running migrations..."
python manage.py migrate --noinput
echo "Starting Gunicorn..."
gunicorn resume_parser.wsgi
