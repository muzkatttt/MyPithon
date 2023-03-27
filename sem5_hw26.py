"""
Задача 26: Напишите программу, которая на вход принимает
два числа A и B, и возводит число А в целую степень B с
помощью рекурсии.

"""

def degree_of_number(a: int, b: int):
    if b == 0:
        return 1
    elif b == 1:
        return a
    return degree_of_number(a, b - 1) * a
a = int(input(f'Введите натуральное число a: \n'))
b = int(input(f'Введите натуральное число b: \n'))
print(degree_of_number(a, b))
