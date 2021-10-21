import random

option = input('Целое, вещественное или символ: ')
if option.lower() in 'целое':
    start = input('Начало диапозона: ')
    finish = input('Конец диапозона: ')
    print(f'{random.randint(int(start), int(finish))} - целое число')
elif option.lower() in 'вещественное':
    start = input('Начало диапозона: ')
    finish = input('Конец диапозона: ')
    print(f'{random.randint(int(start), int(finish))} - вещественное число')
elif option.lower() in 'символ':
    start = input('Превый символ диапозона: ')
    finish = input('Последний символ диапозона: ')
    print(f'{chr(random.randint(ord(start), ord(finish)))} - символ')
