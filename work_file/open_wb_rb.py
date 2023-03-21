# открываем файл для записи байтов
with open('bytes.txt', 'wb') as f:
    pass

with open('bytes.txt', 'rb') as f:
    pass

# открываем файл в текстовом режиме с указанием кодировки
with open('bytes.txt', 'r', encoding='utf-8') as f:
    pass

# запись байтов в файл
f.write(b'some bytes') # файл открыт в режиме wb
f.write('some str') # файл открыт в режиме w
# в любом случае информация хранится в виде 0 и единиц
