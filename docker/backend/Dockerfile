
# docker/backend/Dockerfile
FROM python:3.8

# RUN apt-get update
# RUN apt-get install ffmpeg libsm6 libxext6 espeak  -y

RUN apt update -q \
    && apt install --no-install-recommends -yq espeak \
    libespeak-dev \
    ffmpeg
RUN apt install -yq gcc

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app
COPY ./backend/requirements.txt /app/backend/

RUN pip install numpy==1.23.4
RUN pip install pytest==7.1.3

RUN pip install --upgrade pip && \
    pip install -r backend/requirements.txt

COPY ./docker /app/docker
COPY ./backend /app/backend

EXPOSE 8000