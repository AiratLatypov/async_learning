import asyncpg
import os


async def create_connection():
    connection = await asyncpg.connect(
        host=os.getenv("DATABASE_HOST"),
        port=os.getenv("DATABASE_PORT"),
        user=os.getenv("DATABASE_USER"),
        password=os.getenv("DATABASE_PASSWORD"),
        database=os.getenv("PRODUCTS_DB_NAME")
    )
    return connection
