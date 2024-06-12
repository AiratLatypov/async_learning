import asyncio
import aiohttp

from utils import async_timed
from chapter_04.send_request_with_aiohttp import fetch_status


@async_timed()
async def main():
    """
    При таймоуте wait не снимает сопрограммы.
    Также не вызываются исключения, те что не завершились в результате таймаута отправляются в pending.
    Если нам нужно снять задачи, то придется обойти pending и снять задачу, используя cancel.
    """

    async with aiohttp.ClientSession() as session:
        url = "https://google.com"
        fetchers = [
            asyncio.create_task(fetch_status(session, url)),
            asyncio.create_task(fetch_status(session, url)),
            asyncio.create_task(fetch_status(session, url, 3)),
        ]
        done, pending = await asyncio.wait(fetchers, timeout=1)

        print(f"Число завершившихся задач: {len(done)}")
        print(f"Число ожидающих задач: {len(pending)}")

        for done_task in done:
            result = await done_task
            print(result)


asyncio.run(main())
