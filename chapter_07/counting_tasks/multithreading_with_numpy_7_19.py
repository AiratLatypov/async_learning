import functools
from concurrent.futures.thread import ThreadPoolExecutor
import numpy as np
import asyncio
from utils import async_timed


def mean_for_row(arr, row):
    return np.mean(arr[row])


data_points = 4_000_000_000
rows = 50
columns = int(data_points / rows)

matrix = np.arange(data_points).reshape(rows, columns)


@async_timed()
async def main():
    loop = asyncio.get_running_loop()
    with ThreadPoolExecutor() as pool:
        tasks = []
        for i in range(rows):
            mean = functools.partial(mean_for_row, matrix, i)
            tasks.append(loop.run_in_executor(pool, mean))

        results = asyncio.gather(*tasks)


asyncio.run(main())

# <function main at 0x00000286DE3B6FC0> завершилась за 41.8737 сек
# получилось быстрее более чем в 2 раза
