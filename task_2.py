first_array = [8, 3, 15, 6, 4, 2]
second_array = []
for i in first_array:
    if i % 2 == 0:
        second_array.append(first_array.index(i))

print(second_array)
