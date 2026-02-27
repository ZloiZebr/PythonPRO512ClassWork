import requests

# Получаем список задач для пользователя с ID 1
response = requests.get('https://jsonplaceholder.typicode.com/users/1/todos')

if response.status_code == 200:
    todos = response.json()
    # print(todos[0])
    for task in todos:
        if task['completed']:
            task_status = 'Выполнена'
        else:
            task_status = 'Не выполнена'
        print(f'Задача {task['id']}: {task['title']} >> {task_status}')

else:
    print(f'Ошибка: {response.status_code}')

new_task = {
    'userId': 1,
    'title': 'Купить молоко',
    'completed': False
}

response = requests.post('https://jsonplaceholder.typicode.com/todos', json=new_task)
print(f'Статус: {response.status_code}')
print(response.json())
