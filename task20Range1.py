winners = ['Max', 'Leo', 'Kate']

# простой перебор
for winner in winners:
    print(winner)

# используем range
for i in range(len(winners)):
    # print(i)
    print(i+1, ')', winners[i])

# второй вариант написания кода при использовании range
# range имеет три параметра (start_or_stop, stop, step)
for i in range(1, len(winners) + 1):
    print(i, ')', winners[i-1])
