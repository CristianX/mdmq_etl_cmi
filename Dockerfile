# Utilizar la imagen base de Python 3.8
FROM python:3.8

# Actualizar e instalar las dependencias necesarias, incluyendo debconf-utils para aceptar EULA automáticamente
RUN apt-get update && apt-get install -y unixodbc unixodbc-dev odbcinst odbcinst1debian2 libodbc1 wget debconf-utils

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos de tu proyecto al contenedor
COPY . /app

# Instalar las dependencias de Python desde requirements.txt
RUN pip install -r requirements.txt

# Descargar el controlador ODBC desde Microsoft y aceptar los términos de licencia automáticamente
RUN wget https://packages.microsoft.com/debian/11/prod/pool/main/m/msodbcsql17/msodbcsql17_17.10.5.1-1_amd64.deb -P /tmp/ && \
    echo "msodbcsql17 msodbcsql17/ACCEPT_EULA boolean true" | debconf-set-selections && \
    dpkg -i /tmp/msodbcsql17_17.10.5.1-1_amd64.deb && \
    rm -f /tmp/msodbcsql17_17.10.5.1-1_amd64.deb

# Copiar el resto de archivos del proyecto
COPY . .

# Establecer el punto de entrada para la ejecución de la aplicación
ENTRYPOINT [ "python", "main.py" ]