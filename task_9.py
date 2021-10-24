num_list = [123, 234, 456, 568, 1111111, 32123, 95, 22222333]
list_sum = []
max_num = []
for number in num_list:
    remainder, num_sum = divmod(number, 10)
    while remainder:
        num_sum += remainder % 10
        remainder = remainder // 10
        list_sum.append(num_sum)
    if num_sum > list_sum[0]:
        list_sum.clear()
        list_sum.append(num_sum)
        max_num = (num_sum, number)

print(f'Искомое число - {max_num[1]}, сумма  цифр - {max_num[0]}')
