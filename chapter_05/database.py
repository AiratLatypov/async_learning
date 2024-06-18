import asyncpg
import os

from asyncpg import Pool


async def create_connection():
    connection = await asyncpg.connect(
        host=os.getenv("DATABASE_HOST"),
        port=os.getenv("DATABASE_PORT"),
        user=os.getenv("DATABASE_USER"),
        password=os.getenv("DATABASE_PASSWORD"),
        database=os.getenv("PRODUCTS_DB_NAME")
    )
    return connection


async def create_pool(min_size=6, max_size=6) -> Pool:
    pool: Pool = await asyncpg.create_pool(
        host=os.getenv("DATABASE_HOST"),
        port=os.getenv("DATABASE_PORT"),
        user=os.getenv("DATABASE_USER"),
        password=os.getenv("DATABASE_PASSWORD"),
        database=os.getenv("PRODUCTS_DB_NAME"),
        min_size=min_size,
        max_size=max_size,
    )
    return pool
