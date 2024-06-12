import asyncio
import logging

import aiohttp

from utils import async_timed
from chapter_04.send_request_with_aiohttp import fetch_status


@async_timed()
async def main():
    """
    Функция wait возвращает two sets of Future, done - все завершенные задачи, а pending незавершенные.

    Используя wait мы хотим оборачивать наши корутины в задачи. Иначе wait обернет их самостоятельно, но уже в виде
    нового объекта. Что в некоторых случаях может повлиять на какие-то проверки и условия (новый объект ссылается
    на другое место в памяти).

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
    """Проверка на исключения."""
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


@async_timed()
async def main():
    """
    Работа с флагом FIRST_EXCEPTION. Функция wait вернет результаты сразу по получению исключения.

    Таким образом флаг FIRST_EXCEPTION позволяет нам добавлять логику на случай, если необходимо отменять запросы
    после первой ошибки.
    """

    async with aiohttp.ClientSession() as session:
        fetchers = [
            asyncio.create_task(fetch_status(session, "python://google.com")),
            asyncio.create_task(fetch_status(session, "https://google.com", 3)),
            asyncio.create_task(fetch_status(session, "https://google.com", 3)),
        ]
        done, pending = await asyncio.wait(fetchers, return_when=asyncio.FIRST_EXCEPTION)

        print(f"Число завершившихся задач: {len(done)}")
        print(f"Число ожидающих задач: {len(pending)}")

        for done_task in done:
            if done_task.exception() is None:
                print(done_task.result())
            else:
                logging.error(
                    "При выполенении запроса возникло исключение",
                    exc_info=done_task.exception()
                )

        for pending_task in pending:
            pending_task.cancel()


@async_timed()
async def main():
    """
    Обработка запросов по мере завершения.
    Работа с флагом FIRST_COMPLETED. Функция wait возвращает управление при получении первого результата.
    Остальные задачи останутся в pending.

    Отличие от as_completed как раз в том, что у нас всегда есть информация о том, какие задачи еще не завершились.
    """

    async with aiohttp.ClientSession() as session:
        url = "https://google.com"
        fetchers = [
            asyncio.create_task(fetch_status(session, url)),
            asyncio.create_task(fetch_status(session, url)),
            asyncio.create_task(fetch_status(session, url)),
        ]
        done, pending = await asyncio.wait(fetchers, return_when=asyncio.FIRST_COMPLETED)

        print(f"Число завершившихся задач: {len(done)}")
        print(f"Число ожидающих задач: {len(pending)}")

        for done_task in done:
            print(await done_task)

        # Число завершившихся задач: 1
        # Число ожидающих задач: 2
        # 200


@async_timed()
async def main():
    """
    Обработка всех результатов по мере поступления.
    Выполняем задачи, пока в pending остаются элементы. При каждой итерации pending обновляется.
    """

    async with aiohttp.ClientSession() as session:
        url = "https://google.com"
        pending = [
            asyncio.create_task(fetch_status(session, url)),
            asyncio.create_task(fetch_status(session, url)),
            asyncio.create_task(fetch_status(session, url)),
        ]
        while pending:
            done, pending = await asyncio.wait(pending, return_when=asyncio.FIRST_COMPLETED)

            print(f"Число завершившихся задач: {len(done)}")
            print(f"Число ожидающих задач: {len(pending)}")

            for done_task in done:
                print(await done_task)

            # <function fetch_status at 0x000002414B32FC40> завершилась за 0.4569 сек
            # Число завершившихся задач: 1
            # Число ожидающих задач: 2
            # 200
            # <function fetch_status at 0x000002414B32FC40> завершилась за 0.4659 сек
            # Число завершившихся задач: 1
            # Число ожидающих задач: 1
            # 200
            # <function fetch_status at 0x000002414B32FC40> завершилась за 0.4749 сек
            # Число завершившихся задач: 1
            # Число ожидающих задач: 0
            # 200


asyncio.run(main())
