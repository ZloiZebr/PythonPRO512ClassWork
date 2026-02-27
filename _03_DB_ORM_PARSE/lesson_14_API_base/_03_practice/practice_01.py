"""
Задача 1: Создание класса для получения информации о репозиториях на GitHub

Ситуация:

Вы разрабатываете инструмент для анализа активности разработчиков на GitHub.
Вам нужно получить список репозиториев пользователя, их описания, язык программирования и количество звёзд.

Используйте следующий код для тестирования инструмента:

# Пример использования
if __name__ == "__main__":
    github = GitHubAPI()
    username = input("Введите имя пользователя GitHub: ")
    repos = github.get_user_repos(username)

    if repos:
        print(f"Репозитории пользователя {username}:")
        for repo in repos:
            print(f"Название репозитория: {repo['name']}")
            print(f"Описание репозитория: {repo['description']}")
            print(f"Язык репозитория: {repo['language']}")
            print(f"Звёзд: {repo['stars']}")

        github.save_to_json(repos)
    else:
        print("Не удалось получить данные.")

"""
import json

import requests


class GitHubAPI:
    def __init__(self):
        self.base_url = 'https://api.github.com'

    def get_user_repos(self, username):
        url = f'{self.base_url}/users/{username}/repos'
        try:
            response = requests.get(url)
            response.raise_for_status()
            repos = response.json()
            return GitHubAPI._parse_repos(repos)
        except requests.exceptions.RequestException as e:
            print(f'Ошибка при запросе к GitHub API: {e}')
            return None

    """
    Задача 2: Разработка методов класса для получения информации о репозиториях на GitHub

    Ситуация:
    Вы продолжаете разрабатывать класс GitHubAPI. 
    Теперь вам необходимо добавить методы для парсинга репозиториев и сохранения информации в файл.

    Задача:
    Добавьте в класс GitHubAPI инкапсулированный метод, 
    который извлекает информацию из репозиториев. Пропишите метод для сохранения результатов в файл *.json.
    """

    @staticmethod
    def _parse_repos(repos_data):
        repos_info = []
        for repo in repos_data:
            if not repo['description']:
                description = 'No description'
            else:
                description = repo['description']
            repo_info = {
                'name': repo['name'],
                'description': description,  # repo.get('description', 'No description')
                'language': repo.get('language', 'Not specified'),
                'stars': repo['stargazers_count']
            }
            repos_info.append(repo_info)
        return repos_info

    @classmethod
    def save_to_json(cls, data, filename='github_repos.json'):
        with open(filename, 'w', encoding='utf-8') as fp:
            json.dump(data, fp=fp, ensure_ascii=False, indent=4)
        print(f'Данные сохранены в {filename}')


if __name__ == "__main__":
    github = GitHubAPI()
    username = input("Введите имя пользователя GitHub: ")
    repos = github.get_user_repos(username)

    if repos:
        print(f"Репозитории пользователя {username}:")
        for repo in repos:
            print(f"Название репозитория: {repo['name']}")
            print(f"Описание репозитория: {repo['description']}")
            print(f"Язык репозитория: {repo['language']}")
            print(f"Звёзд: {repo['stars']}")
        GitHubAPI.save_to_json(repos)
    else:
        print("Не удалось получить данные.")
