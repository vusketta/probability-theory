from random import *


def take_part():
    batch1 = [1, 1, 1]
    batch2 = [1, 1, 1]
    batch3 = [1, 1, 2]

    batches = [batch1, batch2, batch3]

    while True:
        batch_number, part_number = randint(0, 2), randint(0, 2)

        if batches[batch_number][part_number] != 2:
            break

    return batches[batch_number].count(2) == 1


if __name__ == '__main__':
    tries_number = 1000000
    good_tries = 0
    for i in range(tries_number):
        result = take_part()
        if result:
            good_tries += 1

    model = good_tries / tries_number
    print("Смоделированный результат:", model)
