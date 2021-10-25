for i in range(2, 10):
    exec(f'count_{i} = 0')

for i in range(2, 100):
    for j in range(2, 10):
        if i % j == 0:
            exec(f'count_{j} += 1')

for i in range(2, 10):
    print(f"Счетчик цифры {i} - {eval(f'str(count_{i})')}")
