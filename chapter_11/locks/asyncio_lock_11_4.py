import asyncio
from asyncio import Lock
from utils import delay


async def a(lock: Lock):
    print("Coroutine a waiting to acquire the lock")
    async with lock:
        print("Coroutine a is in the critical section")
        await delay(2)
    print("Coroutine a released the lock")


async def b(lock: Lock):
    print("Coroutine b waiting to acquire the lock")
    async with lock:
        print("Coroutine b is in the critical section")
        await delay(2)
    print("Coroutine b released the lock")


async def main():
    lock = Lock()
    await asyncio.gather(a(lock), b(lock))


asyncio.run(main())

# Output:
# app-1  | Coroutine a waiting to acquire the lock
# app-1  | Coroutine a is in the critical section
# app-1  | Засыпаю на 2 сек
# app-1  | Coroutine b waiting to acquire the lock
# app-1  | Сон в течение 2 сек закончился
# app-1  | Coroutine a released the lock
# app-1  | Coroutine b is in the critical section
# app-1  | Засыпаю на 2 сек
# app-1  | Сон в течение 2 сек закончился
# app-1  | Coroutine b released the lock
