x1, y1 = int(input('x1')), int(input('y1'))
x2, y2 = int(input('x2')), int(input('y2'))
y = y1 - y2
x = x1 - x2
k = y / x
b = y1 - k * x1
print(f'y = {k} * x + ({b})')
