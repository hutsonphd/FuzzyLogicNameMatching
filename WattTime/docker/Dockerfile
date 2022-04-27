# Dockerfile

# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python:3.10.1-buster
RUN pip install --upgrade pip
LABEL version="0.1.0"

# Mounts the application code to the image
COPY . code
WORKDIR /code

# Allows docker to cache installed dependencies between builds
COPY requirements.txt ../requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

# runs the production server
# ENTRYPOINT ["python", "manage.py"]
# CMD ["runserver", "0.0.0.0:8000"]

COPY ./entrypoint.sh /
ENTRYPOINT ["sh", "/entrypoint.sh"]