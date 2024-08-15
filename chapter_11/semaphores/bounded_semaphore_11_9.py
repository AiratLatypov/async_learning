import asyncio
from asyncio import BoundedSemaphore


async def main():
    """Ограниченный семафор выдаст ошибку ValueError, если количество релизов превысит заданный счетчик."""
    semaphore = BoundedSemaphore(1)

    await semaphore.acquire()
    semaphore.release()
    semaphore.release()


asyncio.run(main())

# ValueError: BoundedSemaphore released too many times
