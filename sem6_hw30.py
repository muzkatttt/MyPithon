"""
Задача 30:  Заполните массив элементами арифметической прогрессии.
Её первый элемент, разность и количество элементов нужно ввести с
клавиатуры. Формула для получения n-го члена прогрессии:
an = a1 + (n-1) * d.
Каждое число вводится с новой строки.
Ввод: 7 2 5
Вывод: 7 9 11 13 15
"""

def arithmetic_sequence(el1: int, diff: int, n_el: int):
    print(*range(el1, el1 + diff * n_el, diff))

arithmetic_sequence(el1=int(input('1-й элемент: \n')), diff=int(input('Разность: \n')),
                    n_el=int(input('Количество элементов: \n')))

"""
решение без ввода данных пользователем
arithmetic_sequence(el1: int, diff: int, n_el: int):
    if n_el == 0:
        return 0
    return el1 + arithmetic_sequence(el1 + diff, diff, n_el - 1)

print(arithmetic_sequence(7, 2, 5))
"""