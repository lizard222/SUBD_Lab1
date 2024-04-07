from bson import ObjectId
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['AutoParts']
controlunits = db['ControlUnits']
engines = db['Engines']
gearboxes = db['GearBoxes']


# Поиск двигателя по названию
def searchEngine(nameEngine):
    itemEngine = engines.find_one({'name': nameEngine})
    return itemEngine

# Поиск коробки передач по названию
def searchGearbox(nameGearbox):
    itemGearbox = gearboxes.find_one({'name': nameGearbox})
    return itemGearbox

# Поиск блока управления по его названию
def searchControlUnit(nameCU):
    itemCU = controlunits.find_one({'name': nameCU})
    return itemCU

# Поиск коробок передач, которые работают в паре с двигателем
def searchActorFilms(engines):
    id = engines.get('_id')
    return list(gearboxes.find({'id_en': id}))

# Поиск двигателей, работающих под управлением блока управления
def searchFilmsCinema(controlunits):
    id = controlunits.get('_id')
    return list(engines.find({'id_cu': id}))

# Определение id коробки передач по названию
def getGearboxId(nameGearbox):
    itemGearbox = searchGearbox(nameGearbox)
    id = ObjectId(itemGearbox["_id"])
    return id

# Определение id блока управления по названию
def getControlUnitId(nameCU):
    itemCU = searchControlUnit(nameCU)
    id = ObjectId(itemCU["_id"])
    return id

# Определение id двигателя по имени
def getEngineId(nameEngine):
    itemEngine = searchEngine(nameEngine)
    id = ObjectId(itemEngine["_id"])
    return id


