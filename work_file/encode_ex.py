# в кодировке ascii нельзя кодировать русские буквы
# при s = 'Hello МИР' возникнет ошибка
s = 'Hello world МИР' # b'Hello world \xd0\x9c\xd0\x98\xd0\xa0' МИР-закодирован

# sb = s.encode('ascii')
# чтобы программа была универсальная, надо вводить кодировку utf-8
sb = s.encode('utf-8')
print(sb)
print(type(sb))

# декодирование с помощью функции decode
s = sb.decode('utf-8')
print(s)
print(type(s))