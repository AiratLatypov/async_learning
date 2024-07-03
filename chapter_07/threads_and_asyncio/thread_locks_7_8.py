import functools
import requests
import asyncio
from concurrent.futures import ThreadPoolExecutor
from threading import Lock


from utils import async_timed

counter_lock = Lock()
counter: int = 0


def get_status_code(url: str) -> int:
    global counter
    response = requests.get(url)
    with counter_lock:
        counter += 1
    return response.status_code


async def reporter(request_count: int):
    while counter < request_count:
        print(f"Завершено запросов: {counter}/{request_count}")
        await asyncio.sleep(.5)


@async_timed()
async def main():
    loop = asyncio.get_running_loop()
    with ThreadPoolExecutor() as pool:
        request_count = 200
        urls = ["https://www.google.com/" for _ in range(request_count)]
        reporter_task = asyncio.create_task(reporter(request_count))
        tasks = [
            loop.run_in_executor(pool, functools.partial(get_status_code, url_))
            for url_ in urls
        ]
        results = await asyncio.gather(*tasks)
        await reporter_task
        print(results)
        # Завершено запросов: 0/200
        # ...
        # Завершено запросов: 190/200
        # <function main at 0x000001DCE74D4E00> завершилась за 16.6670 сек

asyncio.run(main())
