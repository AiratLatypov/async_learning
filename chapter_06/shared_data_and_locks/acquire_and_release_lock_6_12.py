from multiprocessing import Process, Value


def increment_value(shared_int: Value):
    shared_int.get_lock().acquire()
    shared_int.value += 1
    shared_int.get_lock().release()


if __name__ == "__main__":
    """
    В данном случае мы избавляемся от состояния гонки. 
    Для этого используем метод acquire, чтобы заблокировать критический участок кода, а затем 
    метод release для освобождения от блокировки.
    Теперь ошибок не будет. Но фактически мы преобразовали конкурентный код в последовательный.
    
    Также можно использовать контекстный менеджер with:
    def increment_value(shared_int: Value):
        with shared_int.get_lock():
        shared_int.value += 1
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
