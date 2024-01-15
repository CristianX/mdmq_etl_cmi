# Utilizar la imagen base de Python 3.8 en Ubuntu
FROM python:3.8

# Establecer la variable de entorno DEBIAN_FRONTEND para evitar la solicitud interactiva
ENV DEBIAN_FRONTEND=noninteractive

# Actualizar e instalar las dependencias necesarias en el contenedor Ubuntu
RUN apt-get update && apt-get install -y unixodbc unixodbc-dev odbcinst odbcinst1debian2 libodbc1 wget && \
    wget https://packages.microsoft.com/debian/11/prod/pool/main/m/msodbcsql17/msodbcsql17_17.10.5.1-1_amd64.deb -P /tmp/ && \
    # Añadir el siguiente comando para aceptar automáticamente el EULA
    ACCEPT_EULA=Y dpkg -i /tmp/msodbcsql17_17.10.5.1-1_amd64.deb

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos de tu proyecto al contenedor
COPY . /app

# Instalar las dependencias de Python desde requirements.txt
RUN pip install -r requirements.txt

# Copiar el resto de archivos del proyecto
COPY . .

# Establecer el punto de entrada para la ejecución de la aplicación
ENTRYPOINT [ "python", "main.py" ]