import asyncio

from chapter_05.database import create_connection


async def main():
    connection = await create_connection()
    version = connection.get_server_version()
    print(f"Подключено! Версия Postgres равна {version}")
    await connection.close()

asyncio.run(main())
