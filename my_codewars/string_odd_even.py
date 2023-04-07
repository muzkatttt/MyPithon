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
def sort_my_string(s: str):
    s = 'CodeWars'
    s1 = list(s.split())
    print(s1)
    odd = list()
    even = list()
    s1[i] = s1[0]
    new_string = ''
    for i in s1:
        if s1[i] % 2 != 0:
            i.append(odd)
        i.append(even)
        print(odd + even)
    #return
sort_my_string('string')