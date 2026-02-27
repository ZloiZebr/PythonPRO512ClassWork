"""
Задача 1: Анализ погоды через OpenWeatherMap API

Ситуация:
Вы разрабатываете консольный инструмент для получения и анализа текущей погоды в любом городе мира.
Инструмент должен:
запрашивать у пользователя название города,
делать запрос к OpenWeatherMap API,
выводить основную информацию о погоде,
сохранять историю запросов в JSON-файл.
Используйте следующий код для тестирования инструмента:

if __name__ == "__main__":
    weather_app = WeatherAPI()
    city = input("Введите город: ")
    weather_data = weather_app.get_weather(city)

    if weather_data:
        print(f"\nПогода в {city}:")
        print(f"Температура: {weather_data['temp']}°C")
        print(f"Ощущается как: {weather_data['feels_like']}°C")
        print(f"Влажность: {weather_data['humidity']}%")

        weather_app.save_to_json(weather_data)
    else:
        print("Не удалось получить данные о погоде.")

Задача 2: Реализация метода get_weather
Ситуация:
Вы продолжаете разрабатывать класс для получения информации о погоде.
Теперь вам предстоит разработать метод, который принимает название города и возвращает словарь с данными:
"""
import os
import json

import requests
from dotenv import load_dotenv


class WeatherAPI:
    def __init__(self, api_key):
        self.base_url = "https://api.openweathermap.org/data/2.5/weather"
        self.api_key = api_key

    def get_weather(self, city):
        params = {
            'q': city,
            'appid': self.api_key,
            'units': 'metric',
            'lang': 'ru',
        }

        try:
            response = requests.get(self.base_url, params=params, timeout=5)
            response.raise_for_status()
            data = response.json()

            return {
                'city': city,
                'temp': data['main']['temp'],
                'feels_like': data['main']['feels_like'],
                'humidity': data['main']['humidity'],
                'pressure': data['main']['pressure'],
                'description': data['weather'][0]['description'],
            }
        except requests.exceptions.HTTPError as e:
            if response.status_code == 404:
                print(f'Город не найден!')
            else:
                print(f'Ошибка API: {e}')
            return None
        except requests.exceptions.ConnectionError:
            print(f'Не удалось подключится к серверу.')
            return None
        except requests.exceptions.Timeout:
            print(f'Превышено время ожидания ответа от сервера')
            return None
        except requests.exceptions.JSONDecodeError:
            print(f'Файл поврежден')
            return None
        except requests.exceptions.RequestException as err:
            print(f'Ошибка при выполнении запроса: {err}')
            return None

    @staticmethod
    def save_to_json(city, data):
        filename = f'weather_{city}.json'
        with open(filename, 'w', encoding='utf-8') as fp:
            json.dump(data, fp, ensure_ascii=False, indent=4)
        print(f'Данные сохранены в файл')


if __name__ == "__main__":
    load_dotenv()
    API_KEY = os.getenv('WEATHER_API_KEY')

    weather_app = WeatherAPI(api_key=API_KEY)
    user_city = input("Введите город: ")
    weather_data = weather_app.get_weather(user_city)

    if weather_data:
        print(f"\nПогода в {user_city}:")
        print(f"Температура: {weather_data['temp']}°C")
        print(f"Ощущается как: {weather_data['feels_like']}°C")
        print(f"Влажность: {weather_data['humidity']}%")
        print(f"Давление: {weather_data['pressure']} mm.")
        print(f"Описание: {weather_data['description']}")

        weather_app.save_to_json(user_city, weather_data)
    else:
        print("Не удалось получить данные о погоде.")
