from multiprocessing import Process, Value, Array
from array import array


def increment_value(shared_int: Value):
    shared_int.value += 1


def increment_array(shared_array: Array):
    for index, integer in enumerate(shared_array):
        shared_array[index] = integer + 1


if __name__ == "__main__":
    """Поскольку здесь в 2 процессах мы обращаемся к разным элементам, то всё отработает хорошо."""

    integer = Value("i", 0)
    integer_array = Array("i", [0, 0])

    procs = [
        Process(target=increment_value, args=(integer,)),
        Process(target=increment_array, args=(integer_array,)),
    ]

    [p.start() for p in procs]
    [p.join() for p in procs]

    print(integer.value)
    print(integer_array[:])
    # 1
    # [1, 1]
