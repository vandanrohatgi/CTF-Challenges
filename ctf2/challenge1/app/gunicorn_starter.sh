#!/bin/sh
gunicorn --chdir app app:app -w 10 --threads 10 -b 0.0.0.0:8000
