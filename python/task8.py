from random import *


def circuit_fail():
    if randint(1, 10) <= 3:
        return True
    if randint(1, 10) <= 3:
        return True
    if randint(1, 10) <= 4:
        return True
    # c1 - c2 - c3 - c4
    c1 = randint(1, 10) <= 8
    c2 = randint(1, 10) <= 8
    c3 = randint(1, 10) <= 8
    c4 = randint(1, 10) <= 8
    return not (c1 or c4)


if __name__ == '__main__':
    tries_number = 100000
    good_tries = 0
    for i in range(tries_number):
        result = circuit_fail()
        if result:
            good_tries += 1

    model = good_tries / tries_number
    print("Смоделированный результат:", model)
