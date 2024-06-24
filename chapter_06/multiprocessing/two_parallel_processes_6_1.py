"""Работа с процессами."""

import time

from multiprocessing import Process


def count(count_to: int) -> int:
    start = time.time()
    counter = 0
    while counter < count_to:
        counter += 1

    end = time.time()
    print(f"Закончен подсчет до {count_to} за время {end - start}")
    return counter


if __name__ == "__main__":
    start_time = time.time()

    to_one_hundred_million = Process(target=count, args=(100_000_000,))
    to_two_hundred_million = Process(target=count, args=(200_000_000,))

    # Запустить процесс. Метод возвращает управление немедленно
    to_one_hundred_million.start()
    to_two_hundred_million.start()

    # Ждать завершения процесса. Этот метод блокирует выполнение, пока процесс не завершится.
    # Иначе бы программа закрыла бы оба процесса.
    to_one_hundred_million.join()
    to_two_hundred_million.join()

    end_time = time.time()
    print(f"Полное время работы {end_time - start_time}")

    # Закончен подсчет до 100000000 за время 3.7738373279571533
    # Закончен подсчет до 200000000 за время 7.392092943191528
    # Полное время работы 7.402811050415039
