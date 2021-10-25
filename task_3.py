from random import randint

random_array = [randint(1, 100) for i in range(10)]
print(random_array)
min_el = random_array.index(min(random_array))
max_el = random_array.index(max(random_array))
random_array[min_el], random_array[max_el] = random_array[max_el], random_array[min_el]
print(random_array)
