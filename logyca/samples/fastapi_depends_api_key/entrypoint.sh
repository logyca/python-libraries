#!/bin/bash

# Web Server for develop
uvicorn --host=0.0.0.0 --port=80 main:app

# Web Server for production
# gunicorn --bind=0.0.0.0:80 --workers 2 --threads 6 --timeout 600 -k uvicorn.workers.UvicornWorker main:app
