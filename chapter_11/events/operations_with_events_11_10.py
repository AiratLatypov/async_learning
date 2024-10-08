import asyncio
import functools
from asyncio import Event


def trigger_event(event: Event):
    event.set()


async def do_work_on_event(event: Event):
    print("Waiting for event...")
    await event.wait()
    print("Performing work!")
    await asyncio.sleep(1)
    print("Finished work!")
    event.clear()


async def main():
    """
    Вызываем метод wait, который блокирует выполнение, пока кто-то не вызовет метод set, означающий, что событие
    произошло.  
    """

    event = Event()
    asyncio.get_running_loop().call_later(5.0, functools.partial(trigger_event, event))
    await asyncio.gather(do_work_on_event(event), do_work_on_event(event))


asyncio.run(main())

# Waiting for event...
# Waiting for event...
# Performing work!
# Performing work!
# Finished work!
# Finished work!
