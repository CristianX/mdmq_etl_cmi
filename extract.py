from sqlalchemy import create_engine, text


def get_connection(base, server, port, database, username, password):
    # Url de conexión con sqlalchemy
    if base == "SQLServer":
        conn_url = f"mssql+pyodbc://{username}:{password}@{server}:{port}/{database}?driver=ODBC+Driver+17+for+SQL+Server"

    if base == "Postgres":
        conn_url = (
            f"postgresql+psycopg2://{username}:{password}@{server}:{port}/{database}"
        )

    if base == "Oracle":
        conn_url = f"oracle+cx_oracle://{username}:{password}@{server}:{port}/?service_name={database}"

    if base == "MySQL":
        conn_url = f"mysql+mysqldb://{username}:{password}@{server}:{port}/{database}"

    engine = create_engine(conn_url)
    return engine


def extract_data(query, base, server, port, database, username, password):
    engine = get_connection(base, server, port, database, username, password)
    print("Conexion ", engine.connect())
    with engine.connect() as connection:
        result = connection.execute(text(query))
        columns = result.keys()
        data = [dict(zip(columns, row)) for row in result]
        return data
