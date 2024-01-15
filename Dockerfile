# Utilizar la imagen base de Python 3.8
FROM python:3.8

# Actualizar e instalar las dependencias necesarias
RUN apt-get update && apt-get install -y unixodbc unixodbc-dev odbcinst odbcinst1debian2 libodbc1 wget

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos de tu proyecto al contenedor
COPY . /app

# Instalar las dependencias de Python desde requirements.txt
RUN pip install -r requirements.txt

# Descargar el archivo msodbcsql17.tar.gz automáticamente durante la construcción de la imagen
RUN wget https://packages.microsoft.com/debian/11/prod/pool/main/m/msodbcsql17/msodbcsql17_17.10.5.1-1_amd64.deb -P /tmp/

# Instalar el controlador ODBC
RUN dpkg -i /tmp/msodbcsql17_17.10.5.1-1_amd64.deb

# Copiar el resto de archivos del proyecto
COPY . .

# Establecer el punto de entrada para la ejecución de la aplicación
ENTRYPOINT [ "python", "main.py" ]
