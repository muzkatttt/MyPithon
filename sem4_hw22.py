"""
Задача 22:
Даны два неупорядоченных набора целых чисел (может быть, с
повторениями). Выдать без повторений в порядке возрастания
все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа.
n - кол-во элементов первого множества.
m - кол-во элементов второго множества.
Затем пользователь вводит сами элементы множеств.
"""

# решение задачи без функций

n = int(input('Введите размер первого множества: \n'))
print('Введите элементы первого множества: ')
size_n = {int(input()) for i in range(n)}
print(type(size_n))
m = int(input('Введите размер второго множества: \n'))
print('Введите элементы второго множества: ')
size_m = set(int(input()) for j in range(m))
print(type(size_m))
print(size_n)
# print(type(size_n)) # проверка типа
print(size_m)
# print(type(size_m)) # проверка типа
# result = size_n & size_m
result = size_n.intersection(size_m)
print(f'В введенных множествах встречаются числа: {list(result)}')

#эталонный вариант
"""
mol = [int(x) for x in input().split()]
n = mol[0]
m = mol[1]
set_1 = set()
set_2 = set()
list_1 = list()
a = [int(x) for x in input().split()]
k = set(a)
for i in k:
   set_1.add(i)
b = [int(x) for x in input().split()]
k1 = set(b)
for i in k1:
   set_2.add(i)
lok = set_1 & set_2
kool = list(lok)
kool.sort()
for i in kool:
   print(i, end=' ')
"""