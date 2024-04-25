from functools import reduce
from random import *
import math


def get_random_mj(_array_n, _m, _k):
    sublist = _array_n.copy()
    shuffle(sublist)
    sublist = sublist[:_m]
    return [sublist.count(i) for i in range(_k + 1)]


def equals(a, b):
    for index in range(1, len(a)):
        if a[index] != b[index]:
            return False
    return True


def product_of_list(list):
    return reduce(lambda x, y: x * y, list)


if __name__ == '__main__':
    n, m, k = 12, 7, 4

    array_n = [1, 4, 3, 2, 4, 3, 1, 2, 3, 2, 4, 1]
    nj = [array_n.count(i) for i in range(n + 1)]
    mj = [0, 2, 1, 3, 1]

    all_tries, good_tries = 1000000, 0
    for i in range(all_tries):
        random_mj = get_random_mj(array_n, m, k)
        if equals(random_mj, mj):
            good_tries += 1

    model = good_tries / all_tries
    print("Смоделированный результат: ", model)

    prod = product_of_list([math.comb(nj[i], mj[i]) for i in range(1, k + 1)])
    mCn = math.comb(n, m)
    solve = prod / mCn
    print("Вычисленный аналитическим способом результат: ", solve)
    print(prod, mCn)

    print(f"Отношение результатов: {(model / solve):.2}")
