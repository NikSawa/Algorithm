from random import randint

my_array = [randint(1, 100) for i in range(100)]
count_list = []
for i in set(my_array):
    count_list.append((my_array.count(i), i))

print(f'Число: {max(count_list)[1]}\n'
      f'частота появления: {max(count_list)[0]}')
