n = int(input())
flag = True
i = 2
while flag:
    if n % i == 0:  # если ост. при дел.n на i = 0 flag = False
        print(i)
    elif i > n // 2:  # делитель чис. не м. прев. введ. ч., дел. на 2
        flag = False
    i += 1
