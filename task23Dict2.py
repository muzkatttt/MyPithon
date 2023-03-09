friend = {
    'name': 'Max',
    'age': 36
}

print(friend)
print(type(friend))

# по ключу выводим значение на экран
print(friend['age'])

# добавить ключ и значение в словарь
friend['has_car'] = True
print(friend)

# изменить значение в словаре
friend['has_car'] = False
print(friend)

# удалить ключ и его значение из словаря
del friend['age']
print(friend)

# проверка наличия ключа и его значения в словаре
if 'has_car' in friend:
    print('есть авто')

""" варианты перебора словаря:
1) по ключам 2) по значениям
3) по параметрам ключ и значение
"""

# по ключам
for key in friend.keys():
    print(key)  # покажет ключ
    print(friend[key])  # покажет значение ключа

# второй способ перебора по ключам
for key in friend:
    print(key)  # покажет ключ
    print(friend[key])  # покажет значение ключа

# по значениям
for val in friend.values():
    print(val)

# перебор по парам ключ и значение
for item in friend.items():
    print(item)

# 2 вариант перебора по парам ключ и значение
for key, val in friend.items():
    print(key)
    print(val)
