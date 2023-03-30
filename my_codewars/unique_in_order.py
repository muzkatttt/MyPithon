"""
Unique In Order
Implement the function unique_in_order which takes as argument
a sequence and returns a list of items without any elements
with the same value next to each other and preserving the
original order of elements.

Уникальные по порядку
Реализуйте функцию unique_in_order, которая принимает в качестве аргумента
последовательность и возвращает список элементов без каких-либо элементов
с одинаковым значением рядом друг с другом и сохранением
исходного порядка элементов.
'AAAABBBCCDAABBB' -> ['A', 'B', 'C', 'D', 'A', 'B']
"""

import numpy as np
def unique_in_order(sequence):
    string = 'AAAABBBCCDAABBB'
    list1 = []
    for i in string:
        if not list1:
            list1.append(i)
        elif list1[-1] != i:
            list1.append(i)
    print(list1)
a = unique_in_order('AAAABBBCCDAABBB')

from itertools import groupby
def unique_order(_iter):
    return [k for k, g in groupby(_iter)]

