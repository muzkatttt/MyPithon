# если модуль лежит в моей папке - просто импортирую
# import myBibl - если в моей папке
# import folder.secondmodul - если в подпапке, то
# указать путь на подпапку
# импортируем модуль из файла filterFunc.py

import func2  # импортируем файл по названию без .py
# from MyPython.func2 import result, filter
# если файл лежит в подпапке, то импортируем через путь:
# from MyPython.lib import var, function
# где MyPython.lib - путь к подпапке, var - название
# переменной, function - название функции
print(func2.numbers)  # func2 - название файла numbers - переменная
func2.filter()  # filter - название функции из файла func2

print(func2.numbers)
filter()
