
cities = {'Las Vegas', 'Paris', 'Moscow', 'Paris', 'Las Vegas'}

print(type(cities))
print(cities)

cities = set(cities)
print(cities)
print(type(cities))

cities = {'Las Vegas', 'Paris', 'Moscow'}
print(cities)


# функция add - добавить элемент в множество

cities = {'Las Vegas', 'Paris', 'Moscow', 'Paris', 'Las Vegas'}
print(cities)

# .add - добавить элемент в множество
cities.add('Izhevsk')
print(cities)

# .remove - удалить элемент из множества
cities.remove('Las Vegas')
print(cities)

# вывести на экран длину множества
print(len(cities))

print('Paris' in cities)  # проверка наличия элемента в множестве

for city in cities:
    print(city)
