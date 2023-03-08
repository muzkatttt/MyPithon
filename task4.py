top5 = 'Первые 5 мест: 1. Иванов 2. Петров 3. Сидоров 4. Орлов 5. Соколов'
# Поздравляем 1. Иванов 2. Петров 3. Сидоров!
start = top5.find('1')
end = top5.find('4')

top3 = top5[start: end]

result = 'Поздравляем {} с успехом!'.format(top3.upper())

print(result)
