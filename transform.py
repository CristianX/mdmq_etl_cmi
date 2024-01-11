import logging


def transform_data(system_name, data):
    try:
        json_data = [{"SISTEMA": system_name, **row} for row in data]
        return json_data
    except Exception as e:
        logging.error(f"Error al transformar datos: {e}", exc_info=True)
        raise
