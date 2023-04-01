"""
Задача 39. Даны два массива чисел. Требуется вывести
те элементы первого массива (в том порядке, в каком
они идут в первом массиве), которых нет во втором
массиве. Пользователь вводит число N - количество
элементов в первом массиве, затем N чисел - элементы
массива. Затем число M - количество элементов во
втором массиве. Затем элементы второго массива
7
3 1 3 4 2 4 12
6
4 15 43 1 15 1

3 3 2 12
(каждое число вводится с новой строки)
"""
n1 = int(input('Введите количество элементов 1-го массива: \n'))
array1 = list()
for _ in range(n1):
    a1 = int(input('Введите элемент массива 1: \n'))
    array1.append(a1)

n2 = int(input('Введите количество элементов 2-го массива: \n'))
array2 = list()
for _ in range(n2):
    a2 = int(input('Введите элемент массива 2: \n'))
    array2.append(a2)


"""
решение с семинара
a = [3, 1, 3, 4, 2, 4, 12]

b = [4, 15, 43, 1, 15, 1]
res = list(filter(lambda x: x not in b, a))
print(res)

# b dnjhjt htitybt
def input_number(msg: str) -> int:
    result = input(msg + ": ")
    while result.isdigit() == False:
        print("Введены некорректные данные. Попробуйте еще раз.")
        result = input(msg + ": ")
    return int(result)

def main():
    n = input_number("Введите кол-во элементов первого множества")
    m = input_number("Введите кол-во элементов второго множества")
    arr1 = [input_number("Введите " + str(i+1) + " элемент 1го мн-ва" ) for i in range(n)]
    arr2 = [input_number("Введите " + str(i+1) + " элемент 2го мн-ва" ) for i in range(m)]
    print(set(arr1).difference(set(arr2)))
    
# еще одно решение задачи на семинаре
n = int(input("Введите кол-во элементов первого множества: "))
m = int(input("Введите кол-во элементов второго множества: "))

array1 = []
print("Введите элементы первого множества: ")
for i in range(n):
    n1 = input()
    array1.append(n1)
print(f"Первое множество: ", *array1)

array2 = []
print("Введите элементы второго множества: ")
for i in range(m):
    n2 = input()
    array2.append(n2)
print(f"Второе множество: ", *array2)

array3 = []
count1 = 0
for i in array1:
    if i not in array2:
        array3.append(i)
        count1 += 1

print(*(array3))
print(count1)

array4 = []
count2 = 0
for i in array2:
    if i not in array1:
        array4.append(i)
        count2 += 1

print(*(array4))
print(count2)

# еще одно решение
n = int(input())  # количество элементов в первом массиве
a = list(map(int, input().split()))  # первый массив
if len(a) != n:
    print("Некорректный ввод первого массива")
    exit()
m = int(input())  # количество элементов во втором массиве
b = set(map(int, input().split()))  # второй массив
if len(b) != m:
    print("Некорректный ввод второго массива")
    exit()

for x in a:
    if x not in b:
        print(x, end=' ')
        
# еще одно решение
    n = input_number("Введите кол-во элементов первого множества")
    m = input_number("Введите кол-во элементов второго множества")
    arr1 = [input_number("Введите " + str(i+1) + " элемент 1го мн-ва" ) for i in range(n)]
    arr2 = [input_number("Введите " + str(i+1) + " элемент 2го мн-ва" ) for i in range(m)]
    print(set(arr1).difference(set(arr2)))
"""
# ну и от Ришата
"""

def input_num(message: str) -> int:
    input_error: bool = True
    while input_error:
        try:
            temp = int(input(message))
        except ValueError:
            print("Вы ввели не число!")
        else:
            input_error = False
            return temp


def input_list(message: str) -> list:
    temp_list = []
    for i in range(input_num('Please input size of ' + message + ': ')):
        temp_list.append(input_num(f'{i + 1} element of {message}: '))
    print('-' * 20)
    return temp_list


def n_minus_m(n_local: list, m_local: list) -> list:
    n_edit = []
    m_local = set(m_local)
    for i in n_local:
        if i in m_local:
            n_edit.append(i)
    return n_edit


n, m = [input_list(x) for x in ('list N', ' list M')]
print(n, m)
n_m = [i for i in n if i not in m]
print(*n_m)
print(*n_minus_m(n, m))

# решение от Алексея
a = int(input('Введите кол-во элементов N множества: '))
musA = set(int(input('Введите элементы N множества: ')) for i in range(a))

b= int(input('Введите кол-во элементов M множества: '))
musB = set(int(input('Введите элементы M множества: ')) for i in range(b))

i = musA.intersection(musB)                              
print(f'Совпадающие элементы в массивах {i}')

l = musA.difference(musB) 
print(f'НЕ cопадающие элементы в массивах {l}')
"""