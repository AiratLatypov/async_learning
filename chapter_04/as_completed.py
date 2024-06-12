import asyncio
import aiohttp

from utils import async_timed
from send_request_with_aiohttp import fetch_status

@async_timed()
async def main():
    async with aiohttp.ClientSession() as session:
        """
        as_completed позволяет получить итератор корутин и ожидать их выполнения по одной и как-то обрабатывать.
        В отличие от gather, который ждет выполнения всех задач. Также можно передавать атрибут timeout.
        
        Из минусов:
        - порядок результатов становится нарушенным.
        - все созданные задачи продолжают работать в фоновом режиме.
        """
        fetchers = [
            fetch_status(session, "https://google.com", 1),  # 3-й аргумент это цифра ожидания
            fetch_status(session, "https://google.com", 1),
            fetch_status(session, "https://google.com", 10),
            fetch_status(session, "https://google.com", 12),
        ]
        for done_task in asyncio.as_completed(fetchers, timeout=2):
            try:
                result = await done_task
                print(result)
            except asyncio.TimeoutError:
                print("Timeout")

        for task in asyncio.tasks.all_tasks():
            print(task)


asyncio.run(main())
