from pymongo import MongoClient
import random


client = MongoClient('localhost', 27017)
db = client['AutoParts']
controlunits = db['ControlUnits']
engines = db['Engines']
gearboxes = db['GearBoxes']
idCU = []
idEn = []

#Данные для блоков управления
name = [
    "22611-5PA0M",
    "0281001306",
    "03G906018CD",
    "036906032AG",
    "03G906018",
    "03G906018CE",
    "03G906018",
    "03D906023",
    "03G906018CD",
    "03C906014B",
    "03C906016BT",
    "03C906014CQ"
]
brand = [
    "BOSCH",
    "VAG",
]


#Заполнение коллекции ControlUnits
for i in range(50):
    controlunit = controlunits.insert_one({
        "name": random.choice(name),
        "brand": random.choice(brand),
    })
    idCU.append(controlunit.inserted_id)


#Данные для двигателей
name = [
    "EA086",
    "EA111",
    "EA113",
    "EA153",
    "EA211",
    "EA360",
    "EA390",
    "EA395",
    "EA398",
    "EA824",
    "EA827",
]

type = [
    "petrol",
    "diesel",
    "petrol",
    "petrol",
    "diesel",
    "petrol",
    "diesel",
    "diesel",
    "petrol",
    "diesel",
    "petrol",
]

capacity = [
    2.0,
    2.5,
    1.6,
    1.4,
    2.8,
    3.2,
    2.3,
    4.2,
    4.4,
    3.0,
    4.0,
]

torque = [
    300,
    350,
    250,
    200,
    450,
    600,
    430,
    780,
    980,
    550,
    770,
]

horsepower = [
    190,
    225,
    110,
    150,
    300,
    310,
    350,
    500,
    600,
    390,
    440,
]

#Заполнение коллекции Engines
for i in range(len(horsepower)):
    controlunit = engines.insert_one({
        "name": name[i],
        "type": type[i],
        "capacity": capacity[i],
        "torque": torque[i],
        "horsepower": horsepower[i],
        "id_cu": idCU[i],
    })
    idEn.append(controlunit.inserted_id) 


#Данные для коробок передач
name = [
    "DSG",
    "DSG",
    "01M",
    "ZF",
    "ZF",
    "ZF",
    "01M",
    "ZF",
    "ZF",
    "DSG",
    "01M",
]

type = [
    "robotic",
    "robotic",
    "mechanical",
    "automatic",
    "automatic",
    "automatic",
    "mechanical",
    "automatic",
    "automatic",
    "robotic",
    "mechanical",
]

gearcount = [
    5,
    5,
    7,
    7,
    7,
    8,
    8,
    8,
    7,
    7,
    6,
]

#Заполнение коллекции GearBox
for i in range(len(horsepower)):
    controlunit = gearboxes.insert_one({
        "name": name[i],
        "type": type[i],
        "gear_count": gearcount[i],
        "id_en": idEn[i],
    })
