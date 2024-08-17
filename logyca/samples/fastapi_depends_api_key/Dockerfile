# Multistage Dockerfile
# Base Image: Debian 11 (Bullseye) with Python 3.11.2 slim variant
# Initial Image Size: python:3.11.2-slim-bullseye - 122MB
# Final Image Size: 433MB

FROM python:3.11.2-slim-bullseye

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