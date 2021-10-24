import random

wish_num = random.randint(0, 101)
count = 10
while count > 0:
    choice = int(input('Угадайте число: '))
    if wish_num == choice:
        print('Вы угадали!')
        break
    elif wish_num > choice:
        print('Загаданное число больше вашего')
    elif wish_num < choice:
        print('Загаданное число меньше вашего')
    count -= 1
else:
    print(f'Вы проиграли! Я загадал - {wish_num}')
