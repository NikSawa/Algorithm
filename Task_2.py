
import cProfile


def without_eratosthenes(x):  # O(n²)
    check_list = []
    i = 1
    while len(check_list) != x + 1:
        i += 1
        check_list.append(i)
        for j in check_list:
            if i % j == 0 and j != i:
                check_list.remove(i)
                break
    return check_list[x]


def eratosthenes(x):  # O(n * logn)
    check_list = []
    simple_list = []
    if x == 0:
        return 'Введите число, начиная с 1'

    for i in range(x * 100):
        check_list.append(i)
    check_list[1] = 0

    i = 2
    while i <= len(check_list) - 1:
        if check_list[i] != 0:
            j = i + i
            while j <= len(check_list) - 1:
                check_list[j] = 0
                j = j + i
        i += 1
    for i in check_list:
        if i != 0:
            simple_list.append(i)
    return simple_list[x]


def check():
    print(eratosthenes(10000))
    print(without_eratosthenes(10000))


if __name__ == '__main__':
    cProfile.run('check()')

# 104743
# 104743
#          5236437 function calls in 14.749 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000   14.749   14.749 <string>:1(<module>)
#         1    1.418    1.418    1.772    1.772 task_2.py:22(eratosthenes)
#         1    0.011    0.011   14.749   14.749 task_2.py:46(check)
#         1    3.829    3.829   12.965   12.965 task_2.py:9(without_eratosthenes)
#         1    0.000    0.000   14.749   14.749 {built-in method builtins.exec}
#   3958448    0.261    0.000    0.261    0.000 {built-in method builtins.len}
#         2    0.000    0.000    0.000    0.000 {built-in method builtins.print}
#   1183240    0.111    0.000    0.111    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#     94741    9.118    0.000    9.118    0.000 {method 'remove' of 'list' objects}
#
