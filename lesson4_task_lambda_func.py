"""
1. В списке хранятся числа. Нужно выбрать только
четнные числа и составить список пар (число, квадрат числа)
пример: 1 2 3 5 8 15 23 38
вывод: [(2, 4), (8, 64), (38, 1444)]

"""
list1 = [1, 2, 3, 5, 8, 15, 23, 38]
result = list()
for i in list1:
    if i % 2 == 0:
        result.append((i, i ** 2))

print(result)


# решение с помощью лямбда-функции

def select(f, col):  # функция возвращает список в котором к каждому элементу применили функцию f
    return [f(x) for x in col]


def where(f, col):  # функция врзвращает только те значения, которые прошли проверку условия f(x)
    return [x for x in col if f(x)]


list3 = [1, 2, 3, 5, 8, 15, 23, 38]
result2 = select(int, list3)
print(result2)
result2 = where(lambda x: x % 2 == 0, result2)
print(result2)
# вызываем функцию select, с помощью нее преобразуем список result2, возвращаем результат в виде котрежей
result2 = select(lambda x: (x, x ** 2), result2)
print(result2)
