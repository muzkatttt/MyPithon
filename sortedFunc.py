# набор чисел
numbers = [1, 5, 5, 3, 9, 7, 11]
# сортировка по возрастанию
print(sorted(numbers))
# сортировка по убыванию
print(sorted(numbers, reverse=True))

# набор строк
names = ['Max', 'Leo', 'Den', 'Kate', 'Sasha']
# сортировка по алфавиту
print(sorted(names))
# сортировка от Я до А
print(sorted(names, reverse=True))

# города и численность населения
cities = [('Moscow', 1000), ('Izhevsk', 50000),
          ('Agryz', 10000)]  # список [] в виде кортежей ()
# такая сортировка сработает по алфавиту
print(sorted(cities))
# как отсортировать численность наcеления? - записать функцию!


def country(city):
    # ключ индекс = 1 (второй ключ в кортеже), т.к. индексы начинаются с 0
    return city[1]


# для того, чтобы отсортировать по ключу 1, после key указываем название
#  функции без параметра
print(sorted(cities, key=country))

# более лаконичная запись через лямбда-функцию
print(sorted(cities, key=lambda city: city[1]))
