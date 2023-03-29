"""
Задача 32: Определить индексы элементов массива (списка),
значения которых принадлежат заданному диапазону
(т.е. не меньше заданного минимума и не больше заданного максимума)
Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0,-9, 8, 10, -9, 0, -5, -5, 7]
Диапазон от 6 до 12
Вывод: [1, 9, 13, 14, 19]

"""

# решение 1 по условиям задачи
#         0  1  2  3   4   5  6  7   8  9  10  11 12 13  14  15  16  17  18  19
list1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9,  0, -5, -5, 7]
print(*list1)
min = 6
max = 12
array = [0]*len(list1)

for i in range(len(list1)):
    if min <= list1[i] <= max + 1:
        array.append(i)
        print(i)

# решение через рандомное заполнение массива
import random

list2 = [random.randint(-10, 11) for i in range(random.randint(10, 20))]
print(list2)
max = int(input('Введите максимум: \n'))
min = int(input('Введите минимум: \n'))
array = []
for i in range(len(list2)):
    if min <= list2[i] <= max:
        array.append(i)
print(f'Количество элементов в массиве в заданном диапазоне равно {len(array)}')
print(f'Индексы элементов в диапазоне: {array}')


# эталонное решение от ГБ - не выводит индексы
list3 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
print(f'список 3 \n {list3}')
min_number = int(input('Введите минимум: \n'))
max_number = int(input('Введите максимум: \n'))
for i in range(len(list3)):
    if min_number <= list3[i] <= max_number:
        print(list3[i])
