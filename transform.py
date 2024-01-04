def transform_data(system_name, data):
    json_data = [{"SISTEMA": system_name, **row} for row in data]

    return json_data
