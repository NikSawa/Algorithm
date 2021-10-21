list_num = [int(input('Первое число')), int(input('Второе число')), int(input('Третье число'))]
for i in range(len(list_num)):
    for m in range(i + 1, len(list_num)):
        if list_num[m] < list_num[i]:
            list_num[m], list_num[i] = list_num[i], list_num[m]

print(list_num)
print(f'{list_num[1]} среднее число')
