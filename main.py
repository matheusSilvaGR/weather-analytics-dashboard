from fastapi import FastAPI
from services.weather_service import buscar_clima

app = FastAPI()

@app.get("/")
def home():
    return {"mensagem": "API funcionando"}

@app.get("/clima")
def clima():
    return buscar_clima()