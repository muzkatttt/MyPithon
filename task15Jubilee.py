# average life expectancy - средняя продолжительность жизни
ale = 71
age = int(input('сколько вам лет: '))

print('У вас юбилей: ', age % 5 == 0)

# not and or

print('У вас НЕ юбилей:', age % 5 != 0)
print('У вас НЕ юбилей', not age % 5 == 0)

# and
print('У вас юбилей и ваш возраст меньше ale:', age % 5 == 0 and age < ale)

# or
print('У вас юбилей или ваш возраст меньше ale', age % 5 == 0 or age < ale)

# приоритет в логических выражениях
print((1 > 2 and (0 < 5 or 0 < 2) and 0 == 0))
