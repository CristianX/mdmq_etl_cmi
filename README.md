# ETL para la sincronización de información en CMI


## Lenguaje, Framework y versión
Lenguaje: Python
Versión: 3.8.10
Framework: N/A

## Ejecución
1. Activar el entorno virtual: (Windows) venv\Scripts\activate; (Linux) source venv/bin/activate (Realizarlo de manera global)
2. Instalar dependencias: pip install -r requirements.txt
3. Ejecutar script: python main.py
4. Terminada la ejecución del script desactivar el entorno virtual con el comando "deactivate"

## Ejecución en Servidor de Contenedores
1. **Construcción de la imagen de docker (Solo se ejecuta una vez)**: docker build -t etl-cmi .
2. **Ejecución del ETL**: docker run etl-cmi --base XXXXX --server XXX.XXX.XXX.XXX --port XXXX --database XXXXX --username XXXX --pasword XXXX --query "XXXXXXXXXXXXX" --system_name "XXXXXX"