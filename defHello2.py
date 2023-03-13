def greeting(say, *args):
    # знак * перед аргументом функции позволяет выводить
    # несколько переменных через кортеж

    print(say, args)


greeting('Hello', 'Leo')

greeting('Hello', 'Leo', 'Max')
greeting('Hello', 'Leo', 'Max', 'Kate')

print('\n')


def get_person(**kwargs):
    for k, v in kwargs.items():
        print(k, v)


get_person(name='Leo', age=20, car='Audi')
