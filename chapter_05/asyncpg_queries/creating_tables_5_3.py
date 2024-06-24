import asyncio

from chapter_05.database import create_connection
from chapter_05.db_schema.sql_for_tables_creation_5_2 import (
    CREATE_BRAND_TABLE,
    CREATE_PRODUCT_TABLE,
    CREATE_PRODUCT_COLOR_TABLE,
    CREATE_PRODUCT_SIZE_TABLE,
    CREATE_SKU_TABLE,
    COLOR_INSERT,
    SIZE_INSERT
)


async def main():
    """
    Работа ведется для бд products. Создана до исполнения файла с помощью psql -c "CREATE TABLE products;".

    execute - корутина, ожидаем выполнение с помощью await.
    """

    connection = await create_connection()

    statements = [
        CREATE_BRAND_TABLE,
        CREATE_PRODUCT_TABLE,
        CREATE_PRODUCT_COLOR_TABLE,
        CREATE_PRODUCT_SIZE_TABLE,
        CREATE_SKU_TABLE,
        COLOR_INSERT,
        SIZE_INSERT,
    ]

    print("Создается база данных product...")
    for statement in statements:
        status = await connection.execute(statement)
        print(status)
    print("База данных product создана!")
    await connection.close()

    # Создается база данных product...
    # CREATE TABLE
    # CREATE TABLE
    # CREATE TABLE
    # CREATE TABLE
    # CREATE TABLE
    # INSERT 0 1
    # INSERT 0 1
    # База данных product создана!


asyncio.run(main())
