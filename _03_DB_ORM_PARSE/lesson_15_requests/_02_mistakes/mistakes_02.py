"""
Тип ошибки 2: Передача API-ключа в URL вместо заголовка

Если указать API-ключ в URL вместо заголовка в headers:

ключ останется в логах сервера и истории браузера (это небезопасно!);
некоторые API отклонят такие запросы с ошибкой 403 Forbidden.
Пример ошибки:
"""
import requests

# Ключ в URL — уязвимость безопасности!
requests.get("https://api.example.com/data?api_key=123")

"""
Решение:
Передавать ключ в заголовке Authorization (или как указано в документации API).
"""

requests.get(
    "https://api.example.com/data",
    headers={"Authorization": "Bearer YOUR_API_KEY"}  # Безопасный способ
)
