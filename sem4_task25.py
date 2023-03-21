"""
Задача N25. Напишите программу, которая принимает на вход строку
и отслеживает, сколько раз каждый символ уже встречался.
Количество повторов добавляется к символам с помощью постфикса формата _n.
Input: a a a b c a a d c d d
Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
Для решения данной задачи используйте функцию .split()

"""

sp = input('Введите строку:\n').split()
result = {}
for i in sp:
    if i in result:
        print(f'{i}_{result[i]}', end=' ')
    else:
        print(i, end=' ')
        result[i] = result.get(i, 0) + 1

# у Ришата
s = input('Please input text: ').split()
d = {}

for i in s:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
    print(f"{i}", end="")
    if d[i] > 1:
        print(f"_{d[i]}", end=" ")
    else:
        print(' ', end="")

# решение у Кирилла
def using_dict(source: str) -> None:

    count_dict = {}
    stack = []
    for index in range(len(source)):
        el = source[index]
        if el.isalnum():
            count_dict[el] = source[:index].count(el)
            stack.append(el if not count_dict[el] else f'{el}_{count_dict[el]}')

    print('From using_dict\t->', ' '.join(stack))


def using_str(sequence: str):

    stack = []
    for index in range(len(sequence)):
        char = sequence[index]
        if not char.isalnum():
            continue
        counter = sequence[:index].count(char)
        stack.append(char if not counter else f'{char}_{counter}')
    print('From using_str\t->', ' '.join(stack))


def main() -> None:
    queue = 'a a a b c a a d c d d'
    using_str(queue)
    using_dict(queue)


if __name__ == '__main__':
    main()