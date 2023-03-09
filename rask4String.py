# Срезы в строках

friend = "Александр"  # строки указываются или в одинарных ' ' или " "

# срез с 1 по 4 элемент
print(friend[1:4])

# срез с начала строки по 4-й элемент
print(friend[:4])

# срез от 3-го элемента до конца строки
print(friend[3:])

# тип среза - класс str
print(type(friend[1:4]))