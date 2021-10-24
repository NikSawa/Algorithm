num = int(input('Введите  число: '))
rever_num = []
for i in range(len(str(num))):
    rever_num.append(divmod(num, 10)[1])
    num = divmod(num, 10)[0]
print(''.join([str(i) for i in rever_num]))
