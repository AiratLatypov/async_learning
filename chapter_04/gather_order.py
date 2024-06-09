import asyncio

from utils import delay


async def main():
    results = await asyncio.gather(delay(3), delay(1))
    print(results)  # Вывод [3, 1]. Gather возвращает объекты в том же порядке, как и передали


asyncio.run(main())
