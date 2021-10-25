matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
min_elem_list = []

for row in range(len(matrix)):
    min_elem_list.append(min(matrix[row]))

print(max(min_elem_list))
