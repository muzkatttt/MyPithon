global_var = 1


def my_f():
    global global_var  # объявляем глобальную переменную внутри функции
    # локальная переменная внутри функции оьбъявляется без global
    local_var = 100
    # можно использовать локальную переменную внутри функции
    print(local_var)
    # глобальная переменная объявлена в модуле
    print(global_var)


my_f()
print(global_var)

print('\n')


def some_f():
    return 10


result = some_f()
print(result)

a = some_f  # записываем функцию в переменную
print(a)

print(type(a()))
print(a())
