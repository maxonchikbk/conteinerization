#comment
FROM python:3.9-alpine
RUN pip install click==7.1.2
RUN pip install Flask==1.1.2

ADD . /app
ENTRYPOINT python /app/app.py runserver 0.0.0.0:8000