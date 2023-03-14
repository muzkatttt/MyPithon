"""
В зависимости от параметра вызывать различные функции скрипта
Параметр ping -> функция выводит pong
2 параметра name <имя> -> функция привестствия пользователя
параметр list показать содержимое текущей директории
"""

import sys, os

def ping():
    print('pong')

def hello(name):
    print('Hello', name)

hello('Leo')

def get_info():
    print(os.listdir())

get_info()

command = sys.argv[1] # параметр отвечает за нашу команду

if command == 'ping':
    ping()
elif command == 'list':
    get_info()
elif command == 'name':
    name = sys.argv[2] # нужно получить имя через третий параметр [2]
    hello(name)
