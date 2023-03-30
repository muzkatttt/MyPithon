"""
функция map

"""

list1 = [x for x in range(1, 20)]
print(list1)

list1 = list(map(lambda x: x + 10, list1))
print(list1)

"""
решение задачи с помощью функции map
С клавиатуры вводится некий набор чисел, в качестве разделителя используется
пробел. Этот набор чисел будет считан в качестве строки.
Как преобразовать list строк в list чисел?
функция .split преобразует строку в список, используя по умолчанию пробел
"""

data = '15 156 96 3 5 8 52 5'
print(data)

data = data.split()
print(data)

# запись с помощью lambda функции
data2 = ' 15 156 96 3 5 8 52 5'
data2 = list(map(int, data2.split()))
print(data)