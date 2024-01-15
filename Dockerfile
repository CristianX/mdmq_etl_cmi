FROM python:3.8

RUN apt-get update && apt-get install -y unixodbc unixodbc-dev freetds-dev tdsodbc

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

# Copiar el resto de archivos del proyecto
COPY . .

ENTRYPOINT [ "python", "main.py" ]