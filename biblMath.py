# импорт отдельных модулей из библиотеки

import task_random as rd
import math

print(math.pi)  # через точку указываем функции из модуля math

print(math.sin(38))

print('\n')

# импорт отдельных модулей из библиотеки c псевдонимом
print(math.pi)  # через точку указываем функции из модуля math

print(math.sin(38))
print(rd.randint(1, 10))  # вызов функции по псевдониму

print('\n')

# вызов всей библиотеки math включая все объекты, классы,
# скрипты, которые есть в бибилиотеке math
# не рекомендуется
# но в этом случае можно указывать модуль
# без указания библиотеки math

"""
from math import *
print(pi)
print(sin(90))
"""
# можно импортировать отдельные классы,
# функции или данные
"""
from random import randint, randrange

prinr(pi)
print(randint(1, 10))
"""
