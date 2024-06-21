import asyncio

import asyncpg
from asyncpg.transaction import Transaction

from chapter_05.database import create_connection


async def main():
    """Ручное управление транзакцией."""

    connection = await create_connection()
    transaction: Transaction = connection.transaction()

    # начинаем транзакцию
    await transaction.start()

    try:
        await connection.execute(
            "INSERT INTO brand VALUES(DEFAULT, 'brand_1')"
        )
        await connection.execute(
            "INSERT INTO brand VALUES(DEFAULT, 'brand_2')"
        )

    except asyncpg.PostgresError:
        print("Ошибка, транзакция откатывается")
        await transaction.rollback()

    else:
        print("Ошибки нет, транзакция фиксируется!")
        await transaction.commit()


    query = "SELECT brand_name FROM brand WHERE brand_name LIKE 'brand%'"
    brands = await connection.fetch(query)
    print(brands)

    await connection.close()

asyncio.run(main())
