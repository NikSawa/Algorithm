while True:
    sign = input('Введите знак операции ')
    if sign not in ['+', '-', '*', '/', '0']:
        print('Вы ввели некорректный знак операции!')
        continue
    elif sign == '0':
        print('Программа завершена')
        break

    first_num = int(input('Введите число '))
    second_num = int(input('Введите число '))
    if sign == '/':
        if second_num == 0:
            print('На ноль делить невозможно, по крайней мере в этом калькуляторе!')
        else:
            print(f'{first_num / second_num}')
    elif sign == '+':
        print(f'{first_num + second_num}')
    elif sign == '-':
        print(f'{first_num - second_num}')
    elif sign == '*':
        print(f'{first_num * second_num}')
