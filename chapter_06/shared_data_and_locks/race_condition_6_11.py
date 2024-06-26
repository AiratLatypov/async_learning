from multiprocessing import Process, Value


def increment_value(shared_int: Value):
    shared_int.value += 1


if __name__ == "__main__":
    """
    Пример условный, но в какой-то момент возможно значение счетчика не равное 12. Случается это из-за того, что 
    процессы начинают считывать значение переменной integer одновременно, а затем одновременно увеличивают ее
    значение. Получается состояние гонки.
    """

    for _ in range(100):
        integer = Value("i", 0)

        procs = [
            Process(target=increment_value, args=(integer,)),
            Process(target=increment_value, args=(integer,)),
            Process(target=increment_value, args=(integer,)),
            Process(target=increment_value, args=(integer,)),
            Process(target=increment_value, args=(integer,)),
            Process(target=increment_value, args=(integer,)),
            Process(target=increment_value, args=(integer,)),
            Process(target=increment_value, args=(integer,)),
            Process(target=increment_value, args=(integer,)),
            Process(target=increment_value, args=(integer,)),
            Process(target=increment_value, args=(integer,)),
            Process(target=increment_value, args=(integer,)),
        ]

        [p.start() for p in procs]
        [p.join() for p in procs]

        print(integer.value)
        assert integer.value == 12
        # 12
        # 11
        # Traceback (most recent call last):
        #   File "\chapter_06\shared_data_and_locks\race_condition_6_11.py", line 37, in <module>
        #     assert integer.value == 12
        # AssertionError
