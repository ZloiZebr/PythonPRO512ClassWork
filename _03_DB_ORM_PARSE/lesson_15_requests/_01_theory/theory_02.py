import os

import requests
from dotenv import load_dotenv

load_dotenv()
# Ваш API-ключ (вставьте сюда свой ключ; никогда не публикуйте ключи в открытом доступе,
# например в публичных репозиториях на GitHub)

WEATHER_API_KEY = os.getenv('WEATHER_API_KEY')
URL = "https://api.openweathermap.org/data/2.5/weather"

headers = {
    'Authorisation': WEATHER_API_KEY
}

params = {
    'q': 'Новосибирск',
    'appid': WEATHER_API_KEY,
    'units': 'metric'
}

response = requests.get(url=URL, params=params, headers=headers)

if response.status_code == 200:
    data = response.json()
    print(f'Погода в {data['name']}: {data['weather'][0]['description']}')
    print(f'Температура: {data['main']['temp']}°C')
else:
    print(f'Ошибка', response.status_code, response.text)
