FROM python:3.11.9
USER root

# Install git and other necessary dependencies
RUN apt-get update && \
    apt-get -y install git

RUN apt-get update && \
    apt-get -y install --reinstall ca-certificates && \
    apt-get -y install software-properties-common && \
    pip install --upgrade pip

# Install Basic Packages
RUN pip install ipykernel jupyter

# Copy and install requirements
COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt