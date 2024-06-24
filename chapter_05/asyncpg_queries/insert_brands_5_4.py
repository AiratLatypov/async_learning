import asyncio
import asyncpg
import os

from chapter_05.database import create_connection


async def main():
    connection = await create_connection()
    await connection.execute("INSERT INTO brand VALUES(DEFAULT, 'Levis')")
    await connection.execute("INSERT INTO brand VALUES(DEFAULT, 'Seven')")

    brand_query = "SELECT brand_id, brand_name FROM brand"
    results: list[asyncpg.Record] = await connection.fetch(brand_query)

    for brand in results:
        print(f"id: {brand['brand_id']}, name: {brand['brand_name']}")

        # id: 1, name: Levis
        # id: 2, name: Seven

    await connection.close()

asyncio.run(main())
