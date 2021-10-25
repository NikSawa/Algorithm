matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

for row in range(len(matrix)):
    matrix[row].append(sum(matrix[row]))

print('\n'.join('\t'.join(map(str, row)) for row in matrix))
