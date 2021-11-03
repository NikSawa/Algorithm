
import cProfile
import random


def two_min_el():  # O(n) я так понимаю, что тут не n²
    my_array = [random.randint(-100, 100) for _ in range(1000000)]
    print(f'{sorted(my_array)[0]}, {sorted(my_array)[1]}')


def another_tme():  # O(n)
    my_array = [random.randint(-100, 100) for _ in range(1000000)]
    new_array = sorted(my_array).copy()
    print(f'{new_array[0]}, {new_array[1]}')


def another_2_tme():  # O(n) быстрее остальных
    my_array = [random.randint(-100, 100) for _ in range(1000000)]
    first = min(my_array)
    my_array.remove(first)
    second = min(my_array)
    return print(first, second)


def check():
    two_min_el()
    another_tme()
    another_2_tme()


if __name__ == '__main__':
    cProfile.run('check()')

    # 15822536 function calls in 8.492 seconds

#  Ordered by: standard name
#
#  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#       1    0.000    0.000    8.492    8.492 <string>:1(<module>)
# 3000000    2.699    0.000    5.661    0.000 random.py:174(randrange)
# 3000000    1.048    0.000    6.708    0.000 random.py:218(randint)
# 3000000    2.028    0.000    2.961    0.000 random.py:224(_randbelow)
#       1    0.011    0.011    2.490    2.490 task_1.py:13(another_tme)
#       1    0.327    0.327    2.294    2.294 task_1.py:14(<listcomp>)
#       1    0.000    0.000    2.461    2.461 task_1.py:19(another_2_tme)
#       1    0.342    0.342    2.399    2.399 task_1.py:20(<listcomp>)
#       1    0.061    0.061    8.492    8.492 task_1.py:27(check)
#       1    0.022    0.022    3.480    3.480 task_1.py:8(two_min_el)
#       1    0.425    0.425    3.109    3.109 task_1.py:9(<listcomp>)
#       1    0.000    0.000    8.492    8.492 {built-in method builtins.exec}
#       2    0.061    0.030    0.061    0.030 {built-in method builtins.min}
#       3    0.000    0.000    0.000    0.000 {built-in method builtins.print}
#       3    0.519    0.173    0.519    0.173 {built-in method builtins.sorted}
# 3000000    0.253    0.000    0.253    0.000 {method 'bit_length' of 'int' objects}
#       1    0.014    0.014    0.014    0.014 {method 'copy' of 'list' objects}
#       1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
# 3822516    0.681    0.000    0.681    0.000 {method 'getrandbits' of '_random.Random' objects}
#       1    0.001    0.001    0.001    0.001 {method 'remove' of 'list' objects}
