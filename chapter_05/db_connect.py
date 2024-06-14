import asyncpg
import asyncio
import os


async def main():
    connection = await asyncpg.connect(
        host=os.getenv("DATABASE_HOST"),
        port=os.getenv("DATABASE_PORT"),
        user=os.getenv("DATABASE_USER"),
        password=os.getenv("DATABASE_PASSWORD"),
        database=os.getenv("DATABASE_NAME")
    )
    version = connection.get_server_version()
    print(f"Подключено! Версия Postgres равна {version}")
    await connection.close()

asyncio.run(main())
