import random

my_array = [random.randint(0, 100) for i in range(100)]
print(f'{sorted(my_array)[0]}, {sorted(my_array)[1]}')
