import argparse
from extract import extract_data
from transform import transform_data
from load import load_data


def run_etl(query, server, port, database, username, password, system_name):
    data = extract_data(query, server, port, database, username, password)
    # transformed_data = transform_data()
    # load_data("mandar data")
    # json_data = [{"SISTEMA": system_name, **row} for row in data]
    transformed_data = transform_data(system_name, data)

    print(transformed_data)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ejecución de proceso ETL para CMI")
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
        args.server,
        args.port,
        args.database,
        args.username,
        args.password,
        args.system_name,
    )
