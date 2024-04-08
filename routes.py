from fastapi import APIRouter
from pymongo import MongoClient
from scripts import *
from entities import *
from models import *


client = MongoClient('localhost', 27017)
db = client['AutoParts']
controlunits = db['ControlUnits']
engines = db['Engines']
gearboxes = db['GearBoxes']

apiRtr = APIRouter()

#гет для одного
@apiRtr.get("/controlunit")
async def searchControlunits_One(name):
    return controlunitEntity(controlunits.find_one({'name': f'{name}'}))

@apiRtr.get("/engine")
async def searchEngines_One(name):
    return engineEntity(engines.find_one({'name': f'{name}'}))

@apiRtr.get("/gearbox")
async def searchGearboxes_One(name):
    return gearboxEntity(gearboxes.find_one({'name': f'{name}'}))


@apiRtr.get("/controlunits")
async def searchControlunits():
    return controlunitsEntity(controlunits.find())

@apiRtr.get("/engines")
async def searchEngines():
    return enginesEntity(engines.find())

@apiRtr.get("/gearboxes")
async def searchGearboxes():
    return gearboxesEntity(gearboxes.find())

@apiRtr.post("/engines")
async def insert_engines(engine: Engine):
    idControlUnit = getControlUnitId(engine.id_cu)
    engine.id_cu = idControlUnit
    engines.insert_one(dict(engine))
    return enginesEntity(engines.find())

@apiRtr.post("/gearboxes")
async def insert_gearboxes(gearbox: GearBox):
    idControlUnit = getEngineId(gearbox.id_en)
    gearbox.id_en = idControlUnit
    gearboxes.insert_one(dict(gearbox))
    return gearboxesEntity(gearboxes.find())

@apiRtr.post("/controlunits")
async def insert_controlunits(controlunit: ControlUnit):
    controlunits.insert_one(dict(controlunit))
    return controlunitsEntity(controlunits.find())

@apiRtr.put('/engines')
async def update_engines(name, engine: Engine):
    idEngine = getEngineId(name)
    idControlunit = getControlUnitId(engine.id_cu)
    engine.id_cu = idControlunit
    engines.find_one_and_update({"_id":idEngine}, {"$set": dict(engine)})
    return engineEntity(engines.find_one({"_id": idEngine}))

@apiRtr.put('/gearboxes')
async def update_gearboxes(name, gearbox: GearBox):
    idGearbox = getGearboxId(name)
    idEngine = getEngineId(gearbox.id_en)
    gearbox.id_en = idEngine
    engines.find_one_and_update({"_id":idGearbox}, {"$set": dict(gearbox)})
    return gearboxEntity(gearboxes.find_one({"_id": idGearbox}))

@apiRtr.delete('/engines')
async def delete_engine(name):
    idEngine = getEngineId(name)
    return engineEntity(engines.find_one_and_delete({"_id": idEngine}))

@apiRtr.delete('/gearboxes')
async def delete_gearbox(name):
    idGearbox = getGearboxId(name)
    return gearboxEntity(gearboxes.find_one_and_delete({"_id": idGearbox}))

@apiRtr.delete('/controlunits')
async def delete_controlunit(name):
    idControlunit = getControlUnitId(name)
    return controlunitEntity(controlunits.find_one_and_delete({"_id": idControlunit}))

