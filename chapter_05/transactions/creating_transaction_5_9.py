import asyncio
import logging

from chapter_05.database import create_connection


async def main():
    """Транзакция создается с помощью метода transaction."""

    connection = await create_connection()

    async with connection.transaction():
        await connection.execute(
            "INSERT INTO brand VALUES(DEFAULT, 'brand_1')"
        )
        await connection.execute(
            "INSERT INTO brand VALUES(DEFAULT, 'brand_2')"
        )

    query = "SELECT brand_name FROM brand WHERE brand_name LIKE 'brand%'"
    brands = await connection.fetch(query)
    print(brands)

    await connection.close()


async def main():
    """Намеренно допустим ошибку для проверки работы транзакции."""

    connection = await create_connection()

    try:
        async with connection.transaction():
            insert_brand = "INSERT INTO brand VALUES(9999, 'big_brand')"
            await connection.execute(insert_brand)
            await connection.execute(insert_brand)
    except Exception as exc:
        logging.exception(f"Ошибка при создании транзакции {exc}")
    finally:
        query = "SELECT brand_name FROM brand WHERE brand_name LIKE 'brand%'"
        brands = await connection.fetch(query)
        print(brands)

        await connection.close()


asyncio.run(main())
