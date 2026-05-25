import requests

def buscar_clima():

    url = "https://api.open-meteo.com/v1/forecast"

    params = {
        "latitude": -22.90,
        "longitude": -43.20,
        "current_weather": True
    }

    response = requests.get(url, params=params)

    return response.json()