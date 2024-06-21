import asyncio
import logging

from chapter_05.database import create_connection

async def main():
    connection = await create_connection()

    async with connection.transaction():
        await connection.execute("INSERT INTO brand VALUES(DEFAULT, 'my_new_brand')")

        try:
            async with connection.transaction():
                await connection.execute("INSERT INTO product_color VALUES(1, 'black')")
        except Exception as e:
            logging.warning(f"Ошибка при вставке цвета товара игнорируется", exc_info=e)

    await connection.close()

asyncio.run(main())
