"""
Тип ошибки 1: Отсутствие заголовка Content-Type

Проблема:
Сервер может не распознать формат данных и вернуть ошибку 415 Unsupported Media Type
(если ожидает JSON, а получает текст).

Пример ошибки:
"""
import requests

# API ждет JSON, но заголовок не указан
requests.post("https://api.example.com", data={"key": "value"})
# Сервер отвечает: 415 (т. к. данные ушли как form-data, а не JSON)


"""
Решение:
Всегда указывать Content-Type, если API требует конкретный формат.
"""

requests.post(
    "https://api.example.com",
    json={"key": "value"},
    headers={"Content-Type": "application/json"}  # Теперь сервер поймет данные
)