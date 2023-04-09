"""
Given a string s. You have to return another string
such that even-indexed and odd-indexed characters of
s are grouped and groups are space-separated (see sample below)

Note:
0 is considered to be an even index. All input strings are valid with no spaces

Дана строка s. Вы должны вернуть другую строку таким образом,
чтобы четноиндексированные и нечетноиндексированные символы
s были сгруппированы, а группы разделены пробелами (см. пример ниже).

Примечание:
0 считается четным показателем. Все входные строки допустимы без пробелов

"""

"""
# перевернем половины строк

    s = input('Введите строку:\n')
    n = len(s)
    part_1 = (s[:(n + (n % 2)) // 2])
    part_2 = (s[(n + (n % 2)) // 2:])
    print(part_2 + part_1)

"""


def sort_my_string(s: str) -> str:
    even = [i + 2 for i in range(0, len(str))]
    print(type(even))
    #    i.append(even)
    #    return even

    odd = [i + 2 for i in range(1, len(str))]
    print(odd)
    #    i.append(odd)
    #    return odd
    print(even + odd)


sort_my_string(string='some_string')

# def sort_my_string(s: str):
#     s = 'CodeWars'
#     text = ''.join([i for i in s if s.index(i) % 2]) + ' ' + ''.join([i for i in s if not s.index(i) % 2])
#     print(text)
#
#
# sort_my_string('string')