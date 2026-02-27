"""
Тип ошибки 2: Неправильное использование заголовков (Headers)
Отсутствие заголовков при создании запроса может приводить к ошибкам в работе программы. Например:
отсутствие Content-Type для POST/PUT;

передача API-ключа не в том заголовке.
"""

import requests

# # API ждет JSON, но заголовок не указан
# requests.post(
#     "https://api.example.com",
#     json={"key": "value"},
#     # Забыли добавить: headers={"Content-Type": "application/json"}
# )
#
# # API-ключ передается в URL, а не в headers
# requests.get("https://api.example.com?api_key=123")  # Небезопасно!

"""
Решение:
Всегда проверять требуемые заголовки, сверяться с документацией API.
"""

# requests.post(
#     "https://api.example.com",
#     json={"key": "value"},
#     headers={
#         "Content-Type": "application/json",
#         "Authorization": "YOUR_API_KEY"  # Передача ключа API
#     }
# )
