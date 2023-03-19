"""
Задача 18: Требуется найти в массиве A[1..N]
самый близкий по величине элемент к заданному
числу X. Пользователь в первой строке вводит
натуральное число N – количество элементов в
массиве. В последующих строках записаны N
целых чисел Ai. Последняя строка содержит число X
"""

def element_search():
    n = int(input('Введите число N: \n'))
    list = [i for i in range(1, n, 4)]
    print(list)

    x = int(input('Введите искомое число Х в массиве: \n'))
    if x in list:
        print(f'Cамый близкий по величине элемент к X = {x}')
    else:
        for i in range(1, len(list)):
            if x == list[i]:
                print(f'Cамый близкий по величине элемент к {x} = {list[i]}')
                break
            elif list[i] > x:
                if list[i] - x > x - list[i - 1]:
                    print(f'Cамый близкий по величине элемент к {x} = {list[i - 1]}')
                    break
                elif list[i] - x == x - list[i - 1]:
                    print(f'Cамые близкие по величине элементы к {x} : {list[i - 1]} и {list[i]}')
                    break
                else:
                    print(f'Cамый близкий по величине элемент к {x} = {list[i - 1]}')
                    break

element_search()

# второй вариант решения задачи для шага 1 в массиве
"""
def element_search():
    n = int(input('Введите число N: \n'))
    list = [i for i in range(1, n)]
    print(list)

    x = int(input('Введите искомое число Х в массиве: \n'))
    if x in list:
        print(f'Cамый близкий по величине элемент к X = {x}')
    else:
        if x > len(list):
            print(f'Cамый близкий по величине элемент к {x} = {len(list)}')
        elif x < 1:
            print(f'Cамый близкий по величине элемент к {x} = 1')

element_search()
"""