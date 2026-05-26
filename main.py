from fastapi import FastAPI
from services.weather_service import buscar_clima

from database import engine
from models import Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def home():
    return {"mensagem": "API funcionando"}

@app.get("/clima")
def clima():
    return buscar_clima()