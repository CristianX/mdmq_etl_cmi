import os
import logging
# from dotenv import load_dotenv
from pymongo import MongoClient

# load_dotenv()


def load_data(data, mongo_uri):
    if not data:
        return

    try:
        client = MongoClient(mongo_uri)
        db = client[os.environ.get("MONGO_BDD_NAME")]

        system_name = data[0]["SISTEMA"]
        collection = db[system_name]

        # Inserción por lotes
        batch_size = 1000

        for i in range(0, len(data), batch_size):
            batch = data[i : i + batch_size]
            collection.insert_many(batch)
        logging.info(f"Datos cargados en MongoDB en la colección {system_name}.")

    except Exception as e:
        logging.error(f"Error al cargar datos en MongoDB: {e}", exc_info=True)
