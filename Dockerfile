# Dockerfile
FROM python:3.11-alpine
WORKDIR /app
COPY . .
RUN pip install Flask mysql-connector-python
EXPOSE 5000
CMD ["python", "app.py"]
