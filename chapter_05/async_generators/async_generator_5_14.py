import asyncio

from utils import delay, async_timed


async def positive_integers_async(until: int):
    for integer in range(1, until):
        await delay(integer)
        yield integer


@async_timed()
async def main():
    """
    Асинхронный генератор positive_integers_async и конструкция async for. Асинхронный генератор генерирует корутины.

    """

    async_generator = positive_integers_async(3)
    print(type(async_generator))

    async for number in async_generator:
        print(f"Получено число {number}")

    # <class 'async_generator'>
    # Засыпаю на 1 сек
    # Сон в течение 1 сек закончился
    # Получено число 1
    # Засыпаю на 2 сек
    # Сон в течение 2 сек закончился
    # Получено число 2
    # <function main at 0x7feba543d8a0> завершилась за 3.0035 сек

asyncio.run(main())
