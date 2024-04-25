from random import *


def game():
    if randint(1, 10) <= 3:
        return 'A'
    if randint(1, 10) <= 5:
        return 'B'
    if randint(1, 10) <= 4:
        return 'A'
    return 'N'


if __name__ == '__main__':
    tries_number = 10000000
    a_wins, b_wins = 0, 0
    for i in range(tries_number):
        result = game()
        if result == 'A':
            a_wins += 1
        elif result == 'B':
            b_wins += 1
        else:
            continue

    model_a = a_wins / tries_number
    print("Смоделированный результат для А:", model_a)
    model_b = b_wins / tries_number
    print("Смоделированный результат для B:", model_b)
