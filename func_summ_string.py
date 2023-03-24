"""напишите функцию, которая принимает аргументы
в виде букв и выводит в консоль слова
"""

def sum_str(*args): # * обозначает множество аргументов
    res = ' '
    for i in args:
        res += i
    return res
print(sum_str('q', 'e', 'l'))
print(sum_str('q', 'e', 'l', 'e'))
# print(sum_str(1, 8, 9)) выдаст ошибку типов


