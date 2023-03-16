"""
Задача 16: Требуется вычислить, сколько раз
встречается некоторое число X в массиве A[1..N].
Пользователь в первой строке вводит
натуральное число N – количество элементов
в массиве. В последующих строках записаны N
целых чисел Ai.
Последняя строка содержит число X

"""
def how_much_num():
    n = int(input('Введите размер массива: \n'))
    print('Введите элементы массива: ')
    results = [int(input()) for i in range(n)]
    x = int(input('Какое число ищем в массиве? \n'))
    print(list(results))
    count = 0

    while count <= n:
        for elem in results[:]:
            if elem == x:
                count += 1
                print(f'Число {x} встречается {int(count)} раз')

            else:
                if elem == 0:
                    print(f'Числа {x} нет в массиве')
                    count += 1
        return results

how_much_num()
