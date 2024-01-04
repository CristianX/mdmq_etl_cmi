from sqlalchemy import create_engine

SERVER = "172.22.16.110"
PORT = "1433"
DATABASE = "MDMQ_SEGUIMIENTO_AUDITORIA"
USERNAME = "SMSRUsuario"
PASSWORD = "$M$RUsuario"

# Url de conexión con sqlalchemy
conn_url = f"mssql+pyodbc://{USERNAME}:{PASSWORD}@{SERVER}/{DATABASE}?driver=ODBC+Driver+17+for+SQL+Server"

engine = create_engine(conn_url)

# Conexión
with engine.connect() as connection:
    result = connection.execute("SELECT * FROM SRA_USUARIO")
    for row in result:
        print(row)
