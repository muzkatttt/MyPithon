# математические операции (расчеты продолжительности жизни)

# средняя продолжительность жизни в России (лет)
ale = 71
age = int(input('Сколько вам лет? введите: '))

# +
after20 = age + 20
print('через 20 лет вам будет', after20)

# -
alive = ale - age
print('По статистике вам осталось жить', alive)

# * умножение
count = 144000000
all_alive = count * ale
print('среднее время жизни всех людей', all_alive)

# / деление c остатком float
live_part = age / ale
print('часть прожитой жизни', live_part)

# // деление без остатка int
live_part = age // ale
print('часть прожитой жизни', live_part)

print(type(live_part))

# % остаток от деления
print(3 % 2)
print(4 % 2)
print(5 % 3)

# ** возведение в степень
print(2**10)
print(3**3)
