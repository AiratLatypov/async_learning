from threading import Lock, Thread, RLock
from typing import List

list_lock = RLock()
# list_lock = Lock()


def sum_list(int_list: List[int]) -> int:
    """
    Используя обычную блокировку мы получим вечное зависание. Это происходит,
    потому что при первом выполнении функции мы захватили блокировку. И при втором прохождении мы будем ждать
    освобождения этой блокировки вечно.

    Заменив обычный Lock на RLock (реэнтрабельный лок) мы можем позволить потоку повторно заходить в блокированный
    участок кода и избежать зависаний.
    """

    print("Waiting to acquire lock...")
    with list_lock:
        print("Acquired lock.")
        if len(int_list) == 0:
            print("Finished summing.")
            return 0
        else:
            head, *tail = int_list
            print("Summing rest of list.")
            return head + sum_list(tail)


thread = Thread(target=sum_list, args=([1, 2, 3, 4],))
thread.start()
thread.join()
