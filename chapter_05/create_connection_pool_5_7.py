import asyncio

from chapter_05.database import create_pool

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
    """Метод acquire выхватывает из пула свободное подключение. По выходе из блока async with подключение будет
    возвращено в пул."""

    async with pool.acquire() as connection:
        return await connection.fetchrow(product_query)


async def main():
    """
    Кэшированные подключения к бд называются пулом подключений.
    """

    created_pool = await create_pool()
    async with created_pool as pool:
        await asyncio.gather(query_product(pool), query_product(pool))

asyncio.run(main())
