"""
Задача 16: Требуется вычислить, сколько раз
встречается некоторое число X в массиве A[1..N].
Пользователь в первой строке вводит
натуральное число N – количество элементов
в массиве. В последующих строках записаны N
целых чисел Ai.
Последняя строка содержит число X
НЕ ДОДЕЛАЛА
"""
def how_much():
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
                if count == n:
                    print(f'Число {x} встречается {int(count)} раз')

            else:
                print(f'Числа {x} нет в массиве')
                count += 1
        return results

"""
    i = 0
    while count < len(results):
        if x == results[:]:
            count += 1
            print(f'Число {x} встречается {count} раз')
            i += 1

        else:
            count += 1
            print(f'Числа {x} нет в массиве')
            break
        i += 1
"""
how_much()
