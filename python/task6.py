from random import *


def exam():
    questions = [1] * 25 + [0] * 5
    shuffle(questions)

    bilet1 = questions[:2]
    bilet2 = questions[2:4]

    if bilet1.count(1) == 2:
        return True

    if bilet1.count(1) == 1 and bilet2[0] == 1:
        return True

    return False


if __name__ == '__main__':
    tries_number = 100000
    good_tries = 0
    for i in range(tries_number):
        result = exam()
        if result:
            good_tries += 1

    model = good_tries / tries_number
    print("Смоделированный результат:", model)
