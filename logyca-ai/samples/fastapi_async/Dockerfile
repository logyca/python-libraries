FROM python:3.11.10-slim-bookworm

# Set Environment Variables
# Python Configuration
# - PYTHONDONTWRITEBYTECODE: Prevents Python from generating .pyc files
# - PYTHONUNBUFFERED: Ensures Python does not buffer stdout and stderr
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# debconf Configuration: Disable debconf warnings for apt-get
ENV DEBIAN_FRONTEND noninteractive
ENV DEBIAN_PRIORITY critical
ENV DEBCONF_NOWARNINGS yes

# Prepare the Operating System
RUN python -V
RUN apt-get update
RUN pip install --upgrade pip

# OCR Engine
RUN apt-get -y install tesseract-ocr

# Clean the Operating System
RUN rm -rf /var/lib/apt/lists/*

# Copy Source Code
WORKDIR /usr/src/app
COPY . .

# Build Stage
RUN rm -f .env*
RUN pip install -r requirements.txt

# Expose Port for Publication
EXPOSE 80

# Set Entry Point for Container
ENTRYPOINT ["/bin/bash", "entrypoint.sh"]