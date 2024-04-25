from random import *


def balls_distribution():
    balls = [[], [], []]

    for _ in range(9):
        picked_ball = randint(0, 2)
        balls[picked_ball].append(1)

    return balls


if __name__ == '__main__':
    tries_number = 1000000
    a_good_tries, b_good_tries = 0, 0
    for _ in range(tries_number):
        a_result = balls_distribution()
        if a_result[0].count(1) == 3 and a_result[1].count(1) == 3 and a_result[2].count(1) == 3:
            a_good_tries += 1

    for _ in range(tries_number):
        b_result = balls_distribution()
        b_set = set([box.count(1) for box in b_result])
        if {4, 3, 2} == b_set:
            b_good_tries += 1

    model_a = a_good_tries / tries_number
    print("Смоделированный результат для пункта A:", model_a)

    model_b = b_good_tries / tries_number
    print("Смоделированный результат для пункта B:", model_b)
