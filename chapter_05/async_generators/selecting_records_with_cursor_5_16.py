import asyncio

from chapter_05.database import create_connection


async def main():
    """Получаем записи с 501 по 600 с помощью курсора."""

    connection = await create_connection()

    async with connection.transaction():
        query = "SELECT product_id, product_name FROM product"
        # в asyncpg курсор одновременно является и корутиной и генератором, поэтому с ним можно работать и с
        # помощью await и с помощью async for
        cursor = await connection.cursor(query)

        # сдвигаем курсор на 500 записей вперед
        await cursor.forward(500)
        # получаем следующие 100 записей
        products = await cursor.fetch(100)
        for product in products:
            print(product)

    await connection.close()


asyncio.run(main())
