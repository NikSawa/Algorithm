
first = int(input('Введите длину первого отрезка'))
second = int(input('Введите длину второго отрезка'))
third = int(input('Введите длину третьего отрезка'))

if first + second > third and first + third > second and second + third > first:
    if first == second == third:
        print('Равносторонний треугольник')
    elif first == second or second == third or third == first:
        print('равнобедренный треугольник')
    else:
        print('разносторонний треугольник')
else:
    print('Такой треугольник не может существовать')
    