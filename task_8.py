numeric = int(input('Введите число для провекри: '))
number = int(input('Введите цифру, количество которой хотите узнать: '))
count = 0

remainder, check_num = divmod(numeric, 10)
if check_num == number:
    count += 1
while remainder:
    remainder, check_num = divmod(remainder, 10)
    if check_num == number:
        count += 1

print(f'Количество вхождений цифры {number} в число {numeric} - {count}')
