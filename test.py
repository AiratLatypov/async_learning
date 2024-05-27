import asyncio
from utils import delay, async_timed


# @async_timed()
# async def main():
#     sleep_for_three = asyncio.create_task(delay(3))
#     sleep_again = asyncio.create_task(delay(4))
#     sleep_once_more = asyncio.create_task(delay(2))
#
#     await sleep_for_three
#     await sleep_again
#     await sleep_once_more

@async_timed()
async def cpu_bound_work() -> int:
    counter = 0
    for i in range(100_000_000):
        counter += 1
    return counter


@async_timed()
async def main():
    delay_task = asyncio.create_task(delay(4))
    task_one = asyncio.create_task(cpu_bound_work())
    task_two = asyncio.create_task(cpu_bound_work())

    await delay_task
    await task_one
    print(await task_two)

asyncio.run(main(), debug=True)
