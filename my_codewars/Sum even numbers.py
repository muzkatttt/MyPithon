'''
Sum even numbers
Complete the function that takes a sequence of numbers as single parameter.
Your function must return the sum of the even values of this sequence.
Only numbers without decimals like 4 or 4.0 can be even.
The input is a sequence of numbers: integers and/or floats.

Суммировать четные числа
Завершите функцию, которая принимает последовательность чисел
в качестве единственного параметра. Ваша функция должна возвращать
сумму четных значений этой последовательности. Четными могут быть
только числа без десятичных знаков, такие как 4 или 4.0. Входные
данные представляют собой последовательность чисел: целых и/или с плавающей точкой.
'''
def sum_even_numbers(seq):
    my_sum = 0
    for i in seq:
        if i % 2 == 0:
            my_sum += i
    print(seq, ',', my_sum)

sum_even_numbers(seq=[8, 1, 4, 3, 4, 5, 6, 7, 8, 9, 10])


