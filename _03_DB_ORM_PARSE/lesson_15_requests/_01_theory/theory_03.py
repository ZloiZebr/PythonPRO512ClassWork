import requests
from requests.exceptions import RequestException, HTTPError, ConnectionError, Timeout, JSONDecodeError

try:
    response = requests.get('https://api.example.com/data', timeout=5)
    response.raise_for_status()
    data = response.json()
except HTTPError as http_err:
    print(f'HTTP ошибка: {http_err}')
except ConnectionError:
    print(f'Не удалось подключится к серверу.')
except Timeout:
    print(f'Превышено время ожидания ответа от сервера')
except JSONDecodeError:
    print(f'Файл поврежден')
except RequestException as err:
    print(f'Ошибка при выполнении запроса: {err}')
