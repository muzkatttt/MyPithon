"""
Задача 19. Дана последовательность из N целых чисел и число K.
Необходимо сдвинуть всю последовательность
(сдвиг - циклический) на K элементов вправо,
K – положительное число.
Input: [1, 2, 3, 4, 5] k = 3 Output: [4, 5, 1, 2, 3
"""

k = int(input('Укажите сдвиг: \n'))
values = [1, 2, 3, 4, 5]
length = len(values)
k = k % length
print(values)
print(values[-k:] + values[:-k])

# второй вариант решения задачи
k = int(input('Укажите сдвиг: \n'))
values = [1, 2, 3, 4, 5]
length = len(values)
print(values)
print(values[-k:] + values[:-k])