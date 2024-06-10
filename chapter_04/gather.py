import asyncio
from aiohttp import ClientSession

from chapter_04 import fetch_status
from utils import async_timed


@async_timed()
async def main():
    async with ClientSession() as session:
        """Функция gather выдаст все результаты в том же порядке, что и получила. Но будет дожидаться 
        пока не пройдут все запросы."""
        urls = ["https://google.com" for _ in range(1_000)]
        requests = [fetch_status(session, url) for url in urls]
        status_codes = await asyncio.gather(*requests)
        print(status_codes)
        print(len(status_codes))
        # все запрос пройдут за секунд 5-10


@async_timed()
async def main():
    """return_exceptions позволяет также принимать исключения в результат."""
    async with ClientSession() as session:
        urls = ["https://google.com", "python://google.com"]
        requests = [fetch_status(session, url) for url in urls]
        results = await asyncio.gather(*requests, return_exceptions=True)

        exceptions = [res for res in results if isinstance(res, Exception)]
        successful_results = [res for res in results if not isinstance(res, Exception)]

        print(f"All results: {results}")
        print(f"Successful: {successful_results}")
        print(f"Exceptions: {exceptions}")
        # All results: [200, AssertionError()]
        # Successful: [200]
        # Exceptions: [AssertionError()]


asyncio.run(main())
