
def hex_calc(a, b):
    alha_dig_dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5,
                     '6': 6, '7': 7, '8': 8, '9': 9, 'a': 10, 'b': 11,
                     'c': 12, 'd': 13, 'e': 14, 'f': 15}
    a_list = [i for i in a[::-1]]
    b_list = [i for i in b[::-1]]
    result_sum_list = []
    result_mult_list = []
    mult_dict = {}
    remainder = 0

    #  Какой список длинее, чтобы выявить вектор, a_list длиннее
    if len(a_list) <= len(b_list):
        a_list, b_list = b_list, a_list

    # Цикл сложения, перевод в 10-ую систему, счет
    for i in range(len(a_list)):
        if i < len(b_list):
            x = alha_dig_dict[a_list[i].lower()] + alha_dig_dict[b_list[i].lower()] + remainder
        else:
            x = alha_dig_dict[a_list[i].lower()] + remainder
        if x > 15:
            remainder, x = divmod(x, 16)
        else:
            remainder = 0
        result_sum_list.insert(0, x)

    # перевод в 16-ую
    for i in result_sum_list:
        for key, value in alha_dig_dict.items():
            if i == value:
                result_sum_list.remove(i)
                result_sum_list.insert(0, key.upper())

    # Цикл умножения, получение строк результатов умножения
    for i in range(len(b_list)):
        remainder = 0
        for j in range(len(a_list)):
            x = (alha_dig_dict[a_list[j].lower()] * alha_dig_dict[b_list[i].lower()]) + remainder
            if x > 15:
                remainder, x = divmod(x, 16)
            else:
                remainder = 0
            if f'{i}' not in mult_dict.keys():
                mult_dict[f'{i}'] = [x]
            else:
                mult_dict[f'{i}'].append(x)
            if j == len(a_list) - 1 and remainder > 0:
                mult_dict[f'{i}'].append(remainder)

    # добавление 0 в начало для уравнивания разрядности
    for key, value in mult_dict.items():
        count = int(key)
        while count != 0:
            mult_dict[key].insert(0, 0)
            count -= 1

    # Добавление 0 в конец
    for key, value in mult_dict.items():
        count = int(len(mult_dict.keys()) - 1) - int(key)
        while count != 0:
            mult_dict[key].append(0)
            count -= 1

    # сложение строк результатов умножения
    remainder = 0
    for i in range(len(mult_dict['0'])):
        x = 0 + remainder
        for value in mult_dict.values():
            x += value[i]
        if x > 15:
            remainder, x = divmod(x, 16)
        else:
            remainder = 0
        result_mult_list.insert(0, x)

    # перевод в 16-ую
    for i in result_mult_list:
        for key, value in alha_dig_dict.items():
            if i == value:
                result_mult_list.remove(i)
                result_mult_list.insert(0, key.upper())

    return f'сумма - {result_sum_list[::-1]}\n' \
           f'произведение - {result_mult_list[::-1]}'


print(hex_calc('C4F', 'A2'))
