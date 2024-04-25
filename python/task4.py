from random import *


def take_black_try():
    _try = 1
    _bin = ['w', 'b']
    while True:
        if _try == 51:
            return -1
        shuffle(_bin)
        if _bin[0] == 'w':
            _bin.append('w')
            _bin.append('w')
            _try += 1
        else:
            return _try


if __name__ == '__main__':
    tries_number = 100000
    good_tries = 0
    for i in range(tries_number):
        _try = take_black_try()
        if _try == -1:
            good_tries += 1

    model = good_tries / tries_number
    print("Смоделированный результат:", model)
