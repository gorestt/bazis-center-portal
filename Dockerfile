
FROM python:3.10
WORKDIR /app
COPY . .
RUN pip install django gunicorn
CMD ["gunicorn","project.wsgi:application","--bind","0.0.0.0:8000"]
