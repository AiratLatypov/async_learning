import asyncio
from concurrent.futures import ProcessPoolExecutor

from chapter_05.database import create_pool
from utils import async_timed

product_query = \
    """
    SELECT 
    p.product_id, 
    p.product_name, 
    p.brand_id, 
    s.sku_id,
    pc.product_color_name,  
    ps.product_size_name
    FROM product as p
    JOIN sku as s ON p.product_id = s.product_id
    JOIN product_color as pc ON s.product_color_id = pc.product_color_id
    JOIN product_size as ps ON s.product_size_id = ps.product_size_id
    WHERE p.product_id = 100
    """


async def query_product(pool):
    async with pool.acquire() as connection:
        return await connection.fetchrow(product_query)


@async_timed()
async def query_products_concurrently(pool, queries):
    queries = [query_product(pool) for _ in range(queries)]
    return await asyncio.gather(*queries)


def run_in_new_loop(num_queries: int) -> list[dict]:
    async def run_queries():
        created_pool = await create_pool()
        async with created_pool as pool:
            return await query_products_concurrently(pool, num_queries)

    # выполняем запросы в новом цикле событий и преобразовываем их в словари
    results = [dict(result) for result in asyncio.run(run_queries())]
    return results


@async_timed()
async def main():
    """
    Создаем 5 процессов, внутри каждого создается свой event_loop со своим подключением к бд из пула
    для выполнения запросов.
    """
    loop = asyncio.get_event_loop()
    pool = ProcessPoolExecutor()
    # создаем 5 процессов, каждый со своим циклом событий
    tasks = [loop.run_in_executor(pool, run_in_new_loop, 10_000) for _ in range(5)]
    # ждем получения результатов
    all_results = await asyncio.gather(*tasks)
    total_queries = sum([len(result) for result in all_results])
    print(f"Извлечено товаров из базы данных: {total_queries}.")

    # выполняется <function main at 0x7fe748a8bf60> с аргументами () {}
    # выполняется <function query_products_concurrently at 0x7fe7490e0680> с аргументами (<asyncpg.pool.Pool object at 0x7fe74913da60>, 10000) {}
    # выполняется <function query_products_concurrently at 0x7fe7490e0680> с аргументами (<asyncpg.pool.Pool object at 0x7fe74913da60>, 10000) {}
    # выполняется <function query_products_concurrently at 0x7fe7490e0680> с аргументами (<asyncpg.pool.Pool object at 0x7fe74913da60>, 10000) {}
    # выполняется <function query_products_concurrently at 0x7fe7490e0680> с аргументами (<asyncpg.pool.Pool object at 0x7fe74913da60>, 10000) {}
    # выполняется <function query_products_concurrently at 0x7fe7490e0680> с аргументами (<asyncpg.pool.Pool object at 0x7fe74913da60>, 10000) {}
    # <function query_products_concurrently at 0x7fe7490e0680> завершилась за 2.6086 сек
    # <function query_products_concurrently at 0x7fe7490e0680> завершилась за 2.6103 сек
    # <function query_products_concurrently at 0x7fe7490e0680> завершилась за 2.6289 сек
    # <function query_products_concurrently at 0x7fe7490e0680> завершилась за 2.6270 сек
    # <function query_products_concurrently at 0x7fe7490e0680> завершилась за 2.6362 сек
    # Извлечено товаров из базы данных: 50000.
    # <function main at 0x7fe748a8bf60> завершилась за 3.0058 сек


if __name__ == "__main__":
    asyncio.run(main())
