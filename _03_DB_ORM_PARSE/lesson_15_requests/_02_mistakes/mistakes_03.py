"""
Тип ошибки 3: Игнорирование тайм-аута (timeout)

Запрос может висеть бесконечно, если сервер не отвечает, что приведет к зависанию программы.

Пример ошибки:
"""
import requests

# Без timeout программа может зависнуть
requests.get("https://api.example.com/slow-endpoint")  # Ждет вечно...

"""
Решение:
Всегда устанавливать разумный timeout (например, 5–10 секунд):
"""

requests.get("https://api.example.com/slow-endpoint", timeout=5)
# Через 5 сек. выбросится исключение Timeout
