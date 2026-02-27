"""
Тип ошибки 4: Отсутствие обработки ошибок 4xx/5xx
Программа прервет свою работу при получении ошибки сервера (например, 404 Not Found или 500 Internal Server Error).
Пример ошибки:
"""
import requests

# response = requests.get("https://api.example.com/invalid-url")
# data = response.json()  # Ошибка, если response.status_code == 404

"""
Решение:
Использовать raise_for_status() или проверять статус вручную:
"""
try:
    response = requests.get("https://api.example.com/invalid-url", timeout=5)
    response.raise_for_status()
    data = response.json()
except requests.exceptions.HTTPError as http_err:
    print(f'HTTP ошибка: {http_err}')
except requests.exceptions.ConnectionError:
    print('Не удалось подключиться к серверу')
except requests.exceptions.Timeout:
    print('Превышено время ожидания ответа от сервера')
except requests.exceptions.JSONDecodeError:
    print(f'Файл поврежден или неверный формат файла')
except requests.exceptions.RequestException as err:
    print(f'Ошибка при выполнении запроса: {err}')