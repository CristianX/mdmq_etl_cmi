FROM python:3.8

RUN apt-get update && apt-get install -y unixodbc unixodbc-dev odbcinst odbcinst1debian2 libodbc1

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

# Copiar el resto de archivos del proyecto
COPY . .

ENTRYPOINT [ "python", "main.py" ]