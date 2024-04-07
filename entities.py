def controlunitEntity(item) -> dict:
    return {
        "ID":str(item["_id"]),
        "Name":str(item["name"]),
        "Brand":str(item["brand"])
    }

def controlunitsEntity(entity) -> list:
    return [controlunitEntity(item) for item in entity]

def engineEntity(item) -> dict:
    return {
        "ID":str(item["_id"]),
        "Name":str(item["name"]),
        "Type":str(item["type"]),
        "Capacity":float(item["capacity"]),
        "Torque":int(item["torque"]),
        "Horsepower":int(item["horsepower"]),
        "ControlUnit":str(item["id_cu"])
    }

def enginesEntity(entity) -> list:
    return [engineEntity(item) for item in entity]


def gearboxEntity(item) -> dict:
    return {
        "ID":str(item["_id"]),
        "Name":str(item["name"]),
        "Gear_count":int(item["gear_count"]),
        "Engine":str(item["id_en"])
    }

def gearboxesEntity(entity) -> list:
    return [gearboxEntity(item) for item in entity]
