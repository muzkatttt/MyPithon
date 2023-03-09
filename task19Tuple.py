friend_name = 'Max'
friends = ['Max', 'Leo', 'Kate']
roles = ('admin', 'guest', 'user')

if 'Max' in friends:
    print('У меня есть друг ')

if 'M' in friend_name:
    print('Буква M есть в имени друга ')

# while
i = 0
while i < len(friends):
    friend = friends[i]
    print(friend)
    i += 1

# for
for friend in friends:
    print(friend)


# для строки
for letter in friend_name:
    print(letter)

# для кортежа
for role in roles:
    print(role)

print('end')
