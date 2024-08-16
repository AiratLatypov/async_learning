import asyncio
from asyncio import Event
from contextlib import suppress


async def trigger_event_periodically(event: Event):
    while True:
        print("Triggering event!")
        event.set()
        await asyncio.sleep(1)


async def do_work_on_event(event: Event):
    while True:
        print("Waiting for event...")
        await event.wait()
        event.clear()
        print("Performing work!")
        await asyncio.sleep(5)
        print("Finished work!")


async def main():
    """
    Мы увидим, что событие активируется и оба исполнителя начинают работать конкурентно. А мы тем временем продолжаем
    генерировать события. Поскольку исполнители заняты, то они не увидят второго возникновения события, пока не закончат
    работу и не вызовут event.wait() второй раз.
    """
    event = Event()
    trigger = asyncio.wait_for(trigger_event_periodically(event), 5.0)

    with suppress(asyncio.TimeoutError):
        await asyncio.gather(do_work_on_event(event), do_work_on_event(event), trigger)


asyncio.run(main())

# Waiting for event...
# Waiting for event...
# Triggering event!
# Performing work!
# Performing work!
# Triggering event!
# Triggering event!
# Triggering event!
# Triggering event!
# Finished work!
# Waiting for event...
# Performing work!
# Finished work!
# Waiting for event...
