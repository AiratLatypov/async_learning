import asyncio
import requests
import functools
from concurrent.futures import ThreadPoolExecutor

from utils import async_timed


def get_status_code(url_: str) -> int:
    response = requests.get(url_)
    return response.status_code


@async_timed()
async def main():
    loop = asyncio.get_running_loop()

    with ThreadPoolExecutor() as pool:
        urls = ["https://www.google.com/" for _ in range(1_000)]
        tasks = [
            loop.run_in_executor(pool, functools.partial(get_status_code, url_))
            for url_ in urls
        ]
        results = await asyncio.gather(*tasks)
        print(results)
        # <function main at 0x7f1c2eb20f40> завершилась за 26.5934 сек


@async_timed()
async def main():
    """
    Также можно передать в качестве исполнителя по умолчанию None. Это позволит упросить код,
    избавившись от участка с with.
    Исполнитель по умолчанию является глобальным, но и существовать он будет до выхода из приложения.
    """
    loop = asyncio.get_running_loop()

    urls = ["https://www.google.com/" for _ in range(1_000)]
    tasks = [
        loop.run_in_executor(None, functools.partial(get_status_code, url_))
        for url_ in urls
    ]
    results = await asyncio.gather(*tasks)
    print(results)
    # <function main at 0x7f1c2eb20f40> завершилась за 26.5934 сек


asyncio.run(main())
