from sqlalchemy import create_engine, text


def get_connection(server, port, database, username, password):
    # Url de conexión con sqlalchemy
    conn_url = f"mssql+pyodbc://{username}:{password}@{server}:{port}/{database}?driver=ODBC+Driver+17+for+SQL+Server"

    engine = create_engine(conn_url)
    return engine


def extract_data(query, server, port, database, username, password):
    engine = get_connection(server, port, database, username, password)
    with engine.connect() as connection:
        result = connection.execute(text(query))
        columns = result.keys()
        data = [dict(zip(columns, row)) for row in result]
        return data
