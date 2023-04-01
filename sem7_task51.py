"""
Задача No51.Напишите функцию same_by(characteristic, objects),
которая проверяет, все ли объекты имеют одинаковое значение
некоторой характеристики, и возвращают True, если это так.
Если значение характеристики для разных объектов отличается - то False.
Для пустого набора объектов, функция должна возвращать True.
Аргумент characteristic - это функция, которая принимает объект и
вычисляет его характеристику.
Ввод: Вывод:
values = [0, 2, 10, 6] same if same_by(lambda x: x % 2, values):
print(‘same’) else:
print(‘different’)

"""

def same_by(characteristic, objects) -> bool:
    return len(set(map(characteristic, objects))) < 2


def main() -> None:
    values = [0, 2, 10, 6]
    if same_by(lambda x: x % 2, values):
        print('same')
    else:
        print('different')


if __name__ == '__main__':
    main()


"""
same_by = lambda characteristic, objects: True if len(set(list(characteristic(i) for i in objects))) <= 1 else False
"""

#task 51 Анатолий решал

def same_by(characteristic, objects) -> bool:
    result = set([characteristic(obj) for obj in objects])
    return len(result) <= 1


if __name__ == "__main__":
    values = [0, 2, 10, 6]
    if same_by(lambda x: x % 2, values):
        print('same')
    else:
        print('different')