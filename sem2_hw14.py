"""
Задача 14: Требуется вывести все целые степени
двойки (т.е. числа вида 2 в степени k),
не превосходящие числа N.

"""
def degree_num():
    n = int(input('Введите число N: \n'))
    count = 1
    while count < n:
        print(count)
        count *= 2

degree_num()
# второй вариант написания кода
"""
n = int(input('Введите число N: '))
list_1 = [i for i in range(1, n) if i % 2 == 0]

print(f'{list_1}')
"""