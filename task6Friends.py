empty_list = []  # объявляем пустой список

# можно объявить список и сраху заполнить его элементами
friends = ['Max', 'Leo', 'Kate']

# тип списка - list
print(type(friends))

# как и в строке для списка доступны индексы
print('Второй друг: ', friends[1])
print('Первый друг с конца: ', friends[-1])

# можно применить срезы
print(friends[1:2])
print(friends[:2])
print(friends[1:])
