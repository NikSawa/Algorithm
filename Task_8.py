year = int(input('Год: '))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(f'{year} високосный')
else:
    print(f'{year} невисокосный')
