char_list = []
for i in range(32, 128):
    if (len(char_list) + 1) % 10 == 0 and len(char_list) > 0:
        char_list.append(f'{chr(i)} - {i} \n')
    else:
        char_list.append(f'{chr(i)} - {i}')

print(' '.join(char_list))
