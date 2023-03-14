import os

# имя операционной системы
print(os.name)

# текущая рабочая директория
print(os.getcwd())

# создаем новый путь, где os.gercwd - текущий путь
# 'new_f' - папка, которую будем создавать
new_path = os.path.join(os.getcwd(), 'new_f')

# создаем новую папкку по новому пути
os.mkdir(new_path)
