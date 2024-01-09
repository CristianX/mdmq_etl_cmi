import os
from dotenv import load_dotenv
import argparse
from extract import extract_data
from transform import transform_data
from load import load_data

load_dotenv()


def run_etl(query, base ,server, port, database, username, password, system_name):
    mongo_uri = os.environ.get("MONGO_URI")

    if not mongo_uri:
        raise ValueError(
            "La cadena de conexión MongoDB no está definida en las variables de entorno"
        )

    data = extract_data(query, base, server, port, database, username, password)

    if data:
        transformed_data = transform_data(system_name, data)
        load_data(transformed_data, mongo_uri)
        print("Data cargada correctamente")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ejecución de proceso ETL para CMI")
    parser.add_argument(
        "--base", required=True, help="Base de datos como: MySQL, Postgres, Oracle, MariaDB"
    )
    parser.add_argument(
        "--server", required=True, help="IP del servidor de Base de Datos"
    )
    parser.add_argument(
        "--port", required=True, help="Puerto del servidor de Base de Datos"
    )
    parser.add_argument(
        "--database", required=True, help="Nombre de la base de datos Base de Datos"
    )
    parser.add_argument(
        "--username",
        required=True,
        help="Nombre de usuario para la conexión de la Base de Datos",
    )
    parser.add_argument(
        "--password",
        required=True,
        help="Contraseña del usuario para la conexión de la Base de Datos",
    )
    parser.add_argument("--query", required=True, help="Consulta SQL a ejecutar")

    parser.add_argument("--system_name", required=True, help="Nombre del sistema")

    args = parser.parse_args()

    run_etl(
        args.query,
        args.base,
        args.server,
        args.port,
        args.database,
        args.username,
        args.password,
        args.system_name,
    )
