from sqlalchemy import create_engine

SERVER = "172.22.16.110"
PORT = "1433"
DATABASE = "MDMQ_SEGUIMIENTO_AUDITORIA"
USERNAME = "SMSRUsuario"
PASSWORD = "$M$RUsuario"

# Url de conexión con sqlalchemy
conn_url = f"mssql+pyodbc://{USERNAME}:{PASSWORD}@{SERVER}/{DATABASE}?driver=ODBC+Driver+17+for+SQL+Server"


# Url de conexión con sqlalchemy para PostgreSQL
# conn_url = f"postgresql+psycopg2://{USERNAME}:{PASSWORD}@{SERVER}:{PORT}/{DATABASE}"

# Url de conexión con sqlalchemy para Oracle
# conn_url = f"oracle+cx_oracle://{USERNAME}:{PASSWORD}@{SERVER}:{PORT}/?service_name={DATABASE}"

# Url de conexión con sqlalchemy para MariaDB
# conn_url = f"mysql+mysqldb://{USERNAME}:{PASSWORD}@{SERVER}:{PORT}/{DATABASE}"

engine = create_engine(conn_url)

# Conexión
with engine.connect() as connection:
    result = connection.execute("SELECT * FROM SRA_USUARIO")
    for row in result:
        print(row)
