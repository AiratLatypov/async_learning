import asyncio
import requests
from utils import async_timed


def get_status_code(url_: str) -> int:
    response = requests.get(url_)
    return response.status_code


@async_timed()
async def main():
    """
    Функция to_thread еще упрощает передачу работы исполнителю пула потоков.
    Достаточно просто передать функцию и аргумент для нее.
    """
    urls = ["https://www.google.com/" for _ in range(1_000)]
    tasks = [asyncio.to_thread(get_status_code, url_) for url_ in urls]
    results = await asyncio.gather(*tasks)
    print(results)

    # <function main at 0x0000023BB18D4540> завершилась за 87.4777 сек (too many requests)

asyncio.run(main())
