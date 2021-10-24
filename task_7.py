length = int(input('Длина ряда: '))
num = 0
for i in range(length + 1):
    num += i

condition = int((length * (length + 1) / 2))

if num == condition:
    print(f'{num} = {condition} \n'
          f'Доказано')
else:
    print('Что-то не так')
