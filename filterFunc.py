# набор чисел пример через кортеж, но функция
# filter работает со всеми форматами

numbers = (1, 2, 3, 4, 5, 6, 7, 8)

# получить только четные числа


def is_even(number):
    return number % 2 == 0


result = filter(is_even, numbers)
print(result)
result = list(result)  # переводит объект в список
print(result)  # вывод на экран данных в виде списка []

# набор строк
names = ['Max', 'Leo', 'Kate']

# вывести в список имена, длиной больше 4-х символов с помощью лямбда-функции
print(list(filter(lambda x: len(x) > 3, names)))

# вывести в список имена, длиной меньше 4-х символов с помощью лямбда-функции
print(list(filter(lambda x: len(x) < 4, names)))
