# мы можем импортировать
import math
# но не можем импортировать наш модуль например на диске С
# import mymodule

# как питон находит модули?
#import sys

#print(sys.path)
#print(type(sys.path))

#for p in sys.path:
#    print(p)

#sys.path.append('D:')
#import mymodule

# задание для закрепления информации
"""
В папке с модулем создать 5 подпапок названия которых состоят
из платформы, на которой запущен интерпретатор, и порядкового номера
начиная с 1: win32_1, win_32_2
"""
import sys, os

name = sys.platform
for i in range(1, 6):
    new_path = os.path.join(os.getcwd(), '{}_{}'.format(name, i))
    os.mkdir(new_path)


