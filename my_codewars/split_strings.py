"""
Complete the solution so that it splits the string into pairs
of two characters. If the string contains an odd number of
characters then it should replace the missing second character
of the final pair with an underscore ('_').

Завершите решение таким образом, чтобы оно разбило строку на пары
по два символа. Если строка содержит нечетное количество символов,
то она должна заменить отсутствующий второй символ последней пары
символом подчеркивания ('_').
"""

def solution(s):
    arr = []
    for i in s:
