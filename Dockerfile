FROM python:3.9
ENV PYTHONUNBUFFERED 1
ENV DJANGO_ENV dev
ENV DOCKER_CONTAINER 1
WORKDIR /app
COPY requirements.txt /app
RUN pip install -r ./requirements.txt --no-cache-dir
COPY ./ /app

EXPOSE 8000
EXPOSE 5555