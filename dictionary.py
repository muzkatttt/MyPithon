# словари - неупорядоченные коллекции произвольных объектов
# с доступом по ключу

dict = {} # создание
dictionary = {'up': '|', 'left': '<-', 'right': '->'}
print(dictionary) # {'up':'|', 'left':'<-', 'right':'->'}
print(dictionary['left'])
dictionary['left'] = '<='
print(dictionary['left']) # <=
# print(dictionary['type']) # KeyError: 'type'
del dictionary['left'] # удаление элемента
d = {}
#d = dict()

d['q']= 'qwerty' # ключ q, значение qwerty
print(d)

d['w']= 'werty' # ключ q, значение qwerty
print(d)

d['w']= 'werty' # ключ q, значение qwerty
print(d['q']) # qwerty
print('\n')
# печать в отформатированном виде
for item in dictionary:
    print('{}: {}'.format(item, dictionary[item]))

# добавление нового элемента в словарь
print(dictionary.items()) # выведет в консоли dict_items([('up', '|'), ('right', '->')])
for (k, v) in dictionary.items(): # k - ключ, v - значение
    print(k, v)