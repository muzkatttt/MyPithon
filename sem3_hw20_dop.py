"""Задача (допольнительная)
Напишите программу, которая принимает на вход две строки
и определяет, являются ли они анаграммами. Знаки препинания,
пробелы и регистр при этом игнорируются.
Пример ввода:
Цари, вино и сало.
Лисица и ворона.
Пример вывода:
YES
"""

def anagram(string):
    string_list = {}
    for i in string.lower():
        if i.isalpha():
            string_list[i] = string_list.get(i, 0) + 1
    return string_list

print("Да, анаграммы" if anagram(input(f'Введите первое предложение:\n'))
                         == anagram(input(f'Введите второе предложение:\n')) else "Нет")

"""
# 2-й вариант решения для слов

def anagram(string):
    string_list = []
    for i in string.lower():
        string_list.append(i)

    dictionary = {}
    for i in string_list:
        if i not in dictionary:
            dictionary[i] = 1
        else:
            dictionary[i] = dictionary[i] + 1

    return dictionary

string1 = input(f'Введите первое слово:\n')
string2 = input(f'Введите второе слово:\n')

str1 = anagram(string1)
str2 = anagram(string2)

if str1 == str2:
    print(f'Введенные слова являются анаграммами')
else:
    print('Нет, не являются')

"""
