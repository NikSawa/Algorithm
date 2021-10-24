num = int(input('Введите натуральное число: '))

even_list = []
odd_list = []
for i in range(len(str(num))):
    if divmod(num, 10)[1] % 2 == 0:
        even_list.append(divmod(num, 10)[1])
    else:
        odd_list.append(divmod(num, 10)[1])
    num = divmod(num, 10)[0]

print(f'{len(even_list)} - четных цифр\n'
      f'{len(odd_list)} - нечетных цифр')
