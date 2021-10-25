import random

my_array = [random.randint(-100, 100) for i in range(100)]
positive_arr = []
negative_arr = []
for i in my_array:
    if i >= 0:
        positive_arr.append(i)
    else:
        negative_arr.append(i)
print(f'максимальный отрицательный элемент: {max(negative_arr)}\n'
      f'индекс элемента: {my_array.index(max(negative_arr))}')
