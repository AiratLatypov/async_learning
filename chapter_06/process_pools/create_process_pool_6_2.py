from multiprocessing import Pool


def say_hello(name: str) -> str:
    return f"Привет, {name}"


if __name__ == "__main__":
    """Чтобы узнать количество потоков можно использовать multiprocessing.cpu_count()"""
    with Pool() as process_pool:
        # метод apply блокирует программу до завершения функции say_hello
        hi_jeff = process_pool.apply(say_hello, args=("Jeff",))
        hi_john = process_pool.apply(say_hello, args=("John",))
        print(hi_jeff)
        print(hi_john)
