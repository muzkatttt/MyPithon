"""
Задача 49.Планеты вращаются вокруг звезд по эллиптическим орбитам.
Назовем самой далекой планетой ту, орбита которой имеет самую большую
площадь. Напишите функцию find_farthest_orbit(list_of_orbits),
которая среди списка орбит планет найдет ту, по которой вращается самая
далекая планета. Круговые орбиты не учитывайте: вы знаете, что у вашей
звезды таких планет нет, зато искусственные спутники были были запущены
на круговые орбиты. Результатом функции должен быть кортеж, содержащий
длины полуосей эллипса орбиты самой далекой планеты. Каждая орбита
представляет из себя кортеж из пары чисел - полуосей ее эллипса.
Площадь эллипса вычисляется по формуле S = pi*a*b,
где a и b - длины полуосей эллипса.
При решении задачи используйте списочные выражения.
Подсказка: проще всего будет найти эллипс в два шага:
сначала вычислить самую большую площадь эллипса, а затем найти и сам эллипс,
имеющий такую площадь. Гарантируется, что самая далекая планета ровно одна

orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(*find_farthest_orbit(orbits))
"""
from math import pi


def find_farthest_orbit(list_of_orbits: list) -> tuple:
    squares_iterable = map(lambda el: pi * el[0] * el[1] if el[0] != el[1] else None, list_of_orbits)
    squares_list = list(squares_iterable)
    max_square = max(filter(lambda el: el is not None, squares_list))
    index_of_max_square = squares_list.index(max_square)
    return list_of_orbits[index_of_max_square]


def main() -> None:
    orbits = [(6, 6), (1, 3), (2.5, 10), (7, 2), (4, 3)]
    print(*find_farthest_orbit(orbits))


if __name__ == '__main__':
    main()

"""
решение от Андрея Крылова 
orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]

orbits_square = lambda orbits: list(int(3.14 * i[0] * i[1]) for i in orbits if i[0] !=  i[1])
print(*orbits_square(orbits))
find_farthest_orbit = lambda array: list(i for i in orbits if int(3.14 * i[0] * i[1]) == min(orbits_square(orbits)))      
print(*find_farthest_orbit(orbits))
"""