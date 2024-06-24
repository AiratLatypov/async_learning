import asyncio

from chapter_05.database import create_connection


async def main():
    """Построчная работа с выборкой из бд с помощью асинхронного генератора."""

    connection = await create_connection()

    query = "SELECT product_id, product_name FROM product"

    async with connection.transaction():
        async for product in connection.cursor(query):
            print(product)

    await connection.close()


asyncio.run(main())
