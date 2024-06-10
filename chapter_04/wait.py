import asyncio
import logging

import aiohttp

from utils import async_timed
from chapter_04.send_request_with_aiohttp import fetch_status


@async_timed()
async def main():
    """
    Функция wait возвращает two sets of Future, done - все завершенные задачи, а pending незавершенные.

    В случае return_when=ALL_COMPLETED функция wait вернет результаты, когда все запросы будут выполнены.
    Если возникнет исключение, то оно не будет возбуждено. Увидеть исключение можно, если применить await для
    ошибочной задаче внутри done.
    """

    async with aiohttp.ClientSession() as session:
        fetchers = [
            asyncio.create_task(fetch_status(session, "https://google.com")),
            asyncio.create_task(fetch_status(session, "https://google.com")),
        ]
        done, pending = await asyncio.wait(fetchers)  # return_when=ALL_COMPLETED

        print(f"Число завершившихся задач: {len(done)}")
        print(f"Число ожидающих задач: {len(pending)}")

        for done_task in done:
            result = await done_task
            print(result)


@async_timed()
async def main():
    async with aiohttp.ClientSession() as session:
        good_request = fetch_status(session, "https://google.com")
        bad_request = fetch_status(session, "python://google.com")

        fetchers = [
            asyncio.create_task(good_request),
            asyncio.create_task(bad_request),
        ]
        done, pending = await asyncio.wait(fetchers)

        print(f"Число завершившихся задач: {len(done)}")
        print(f"Число ожидающих задач: {len(pending)}")

        for done_task in done:
            # result = await done_task возбудит исключение
            if done_task.exception() is None:
                print(done_task.result())
            else:
                logging.error(
                    "При выполенении запроса возникло исключение",
                    exc_info=done_task.exception()
                )


asyncio.run(main())
