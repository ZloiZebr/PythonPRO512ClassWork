"""
Тип ошибки 1: Отсутствие обработки HTTP-ошибок
Проблема:
Когда API возвращают HTTP-коды ошибок (4xx, 5xx) и разработчики их игнорируют,
это приводит к сбоям в работе программы.
"""

import requests

# response = requests.get("https://api.example.com/data")
# data = response.json()  # Ошибка, если response.status_code != 200

"""
Решение:
Прописывать правила для проверки статуса ответа и обработки ошибок:
"""
try:
    response = requests.get("https://api.example.com/data")
    response.raise_for_status()  # Вызовет исключение при 4xx/5xx
    data = response.json()
except requests.exceptions.RequestException as ex:
    print(type(ex).__name__)
