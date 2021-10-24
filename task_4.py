num = 1
count = 0
for i in range(int(input('Длина ряда '))):
    count += num
    num = num / -2
print(count)
