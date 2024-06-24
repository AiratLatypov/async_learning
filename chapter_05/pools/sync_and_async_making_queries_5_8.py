import asyncio

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
async def query_products_synchronously(pool, queries):
    return [await query_product(pool) for _ in range(queries)]


@async_timed()
async def query_products_concurrently(pool, queries):
    queries = [query_product(pool) for _ in range(queries)]
    return await asyncio.gather(*queries)


async def main():
    created_pool = await create_pool()
    async with created_pool as pool:
        await query_products_synchronously(pool, 10_000)
        await query_products_concurrently(pool, 10_000)


asyncio.run(main())

# разница получилась чуть больше чем в 2 раза, в зависимости от системы может быть еще больше
# выполняется <function query_products_synchronously at 0x7f7f0d13f9c0> с аргументами (<asyncpg.pool.Pool object at 0x7f7f0d15f5e0>, 10000) {}
# <function query_products_synchronously at 0x7f7f0d13f9c0> завершилась за 4.7557 сек
# выполняется <function query_products_concurrently at 0x7f7f0cb819e0> с аргументами (<asyncpg.pool.Pool object at 0x7f7f0d15f5e0>, 10000) {}
# <function query_products_concurrently at 0x7f7f0cb819e0> завершилась за 2.2421 сек
