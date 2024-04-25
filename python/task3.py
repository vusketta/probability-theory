from random import *


if __name__ == '__main__':
    T = 1000000
    t = randint(0, T)
    tries_number = 10000000
    all_tries = [(randint(0, T), randint(0, T)) for _ in range(tries_number)]
    good_tries = [(a, b) for (a, b) in all_tries if abs(a - b) <= t]

    model = len(good_tries) / len(all_tries)
    print("Смоделированный результат при t =", t, ":", model)

    solve = 1 - (1 - t / T) ** 2
    print("Вычисленный аналитическим способом результат: ", solve)

    print(f"Отношение результатов: {(model / solve):.2}")
