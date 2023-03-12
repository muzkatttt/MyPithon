# Напишите программу угадай число для одного пользователя

"""# первое решение с помощью цикла и оператора break
# шаг 1
import random

number = random.randint(1, 100)
# print(number)  # для тестирования программы

while True:
    # шаг 2
    user_number = int(input('Введите число: '))
    # print(user_number)

    # шаг 3
    if number == user_number:
        print('Победа!')
        break
    elif number < user_number:
        print('Введенное число больше загаданного')
    else:
        print('Введенное число меньше загаданного')
"""

# второе решение с помощью цикла (оптимальное)

import random

number = random.randint(1, 100)
# print(number)  # для тестирования программы

user_number = None
count = 0
# задаем количество уровней через словарь, где 1 - уровень,
# 10 - ключ - то есть количество попыток
levels = {1: 10, 2: 5, 3: 3}

level = int(input('Введите уровень сложности от 1 до 3: '))
# в [] скобках вводится ключ: либо число либо переменная
max_count = levels[level]  # вводим ограничение на количество попыток


while number != user_number:
    count += 1
    if count > max_count:
        print('Вы проиграли :(')
        break
    print(f'Попытка № {count}')

    user_number = int(input('Введите число: '))
    # print(user_number)

    if number < user_number:
        print('Введенное число больше загаданного')
    elif number > user_number:
        print('Введенное число меньше загаданного')

else:
    print('Победа!')
