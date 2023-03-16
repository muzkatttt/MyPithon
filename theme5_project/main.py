"""
Создайте модуль main.py. Из модулей,
реализованных в модулях folders.py и
randomlist.py, сделайте импорт в main.py
и проверьте, что все работает как надо
"""

import randomlist
from folders import create_folders, delete_folders



"""
при вызове функции в данном модуле в консоли
выводятся результаты из модулей folders.py и
randomlist.py, т.к. в них мы вызываем функции, 
чтобы этого не происходило, для этого необходимо
вывести выражение 
if __name__ == 'main':
и сдвинуть вызов функций под конструкцию выше
create_folders()
delete_folders()
"""
if __name__ == 'main':
    create_folders()
    delete_folders()
print(randomlist.get_random([1, 2, 3, 4]))
print(randomlist.get_random([1]))
print(randomlist.get_random([0]))
"""
тоже самое нужно сделать в модулях folders.py и
randomlist.py и сдвинуть вызов функций под конструкцию
if __name__ == 'main':
"""