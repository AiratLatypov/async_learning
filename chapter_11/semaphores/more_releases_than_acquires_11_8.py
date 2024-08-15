import asyncio
from asyncio import Semaphore


async def acquire(semaphore: Semaphore):
    print("Waiting to acquire")
    async with semaphore:
        print("Acquired")
        await asyncio.sleep(5)
    print("Releasing")


async def release(semaphore: Semaphore):
    print("Releasing as a one off!")
    semaphore.release()
    print("Released as a one off!")


async def main():
    """Количество релизов превышает количество захватов. Из-за чего счетчик семафора уходит в минус. И следующие
    захваты смогут пройти в большем количестве."""
    semaphore = Semaphore(2)

    print("Acquiring twice, releasing three times...")
    await asyncio.gather(
        acquire(semaphore),
        acquire(semaphore),
        release(semaphore),
    )

    print("Acquiring three times...")
    await asyncio.gather(
        acquire(semaphore),
        acquire(semaphore),
        acquire(semaphore),
    )


asyncio.run(main())

# Output
# Acquiring twice, releasing three times...
# Waiting to acquire
# Acquired
# Waiting to acquire
# Acquired
# Releasing as a one off!
# Released as a one off!
# Releasing
# Releasing
# Acquiring three times...
# Waiting to acquire
# Acquired
# Waiting to acquire
# Acquired
# Waiting to acquire
# Acquired
# Releasing
# Releasing
# Releasing
