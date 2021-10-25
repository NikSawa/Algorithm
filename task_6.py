import random

my_array = [random.randint(0, 100) for i in range(100)]
sum_elements = 0
list_elem = [my_array.index(min(my_array)), my_array.index(max(my_array))]

for i in range(sorted(list_elem)[0] + 1, sorted(list_elem)[1]):
    sum_elements += my_array[i]

print(sum_elements)
