from pydantic import BaseModel

class ControlUnit(BaseModel):
    name: str
    brand: str

class Engine(BaseModel):
    name: str
    type: str
    capacity: float
    torque: int
    horsepower: int  
    id_cu: str

class GearBox(BaseModel):
    name: str
    type: str
    gear_count: int
    id_en: str
