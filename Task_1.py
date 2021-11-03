import collections as c


def income_analyze(count):
    income_data = c.defaultdict(list)
    low_income = {}
    high_income = {}
    amount = count
    while amount > 0:
        name = input('Введите название: ')
        for i in range(4):
            income_data[name].append(float(input(f'Прибыль за {i + 1} квартал: ')))
        amount -= 1

    sum_all = 0
    for value in income_data.values():
        sum_all += sum(value)
    avg_income = sum_all / count

    for key, value in income_data.items():
        if sum(value) <= float(avg_income):
            low_income[key] = sum(value)
        else:
            high_income[key] = sum(value)

    return f'Компании чей доход выше среднего {int(avg_income)} \n' \
           f'{high_income} \n' \
           f'Компании чей доход ниже среднего {int(avg_income)} \n' \
           f'{low_income}'


print(income_analyze(4))
