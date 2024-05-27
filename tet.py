import asyncio
from time import sleep
import aiohttp

from dataclasses import dataclass, field
from utils import delay


@dataclass
class Test:
    name: str
    price: float


# loop = asyncio.get_event_loop()
#
#
# async def sleep_func(time):
#     print("Start func 1")
#     await asyncio.sleep(time)
#     print(f"Finish func 1, time: {time}")
#
#
# async def sleep_func_2(time):
#     print("Start func 2")
#     await asyncio.sleep(time)
#     print(f"Finish func 2, time: {time}")

def call_later():
    print("меня вызовут в ближайшее время!")


async def main():
    loop = asyncio.get_running_loop()
    loop.call_soon(call_later)
    loop.slow_callback_duration = .0000005
    await delay(1)
    # await asyncio.gather(
    #     sleep_func(2.1),
    #     #usual_sleep_func(2),
    #     sleep_func_2(2),
    # )

asyncio.run(main(), debug=True)
