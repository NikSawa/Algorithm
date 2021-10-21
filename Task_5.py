first, second = input('2 буквы без пробела').strip('').lower()
print(f'{first} имеет порядковый номер - {ord(first) - 96} \n'
      f'{second} имеет порядковый номер - {ord(second) - 96} \n')
if abs(ord(first) - ord(second)) == 1:
    print(f'{first} и {second} соседние букв')
else:
    print(f'между {first} и {second} {(abs(ord(first) - ord(second)) - 1)} букв')
