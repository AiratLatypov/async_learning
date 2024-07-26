import asyncpg
import os

from asyncpg import Pool
from aiohttp.web_app import Application

DB_KEY = "database"


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


async def add_database_pool_to_app(application: Application):
    print("Creating database pool.")
    pool = await create_pool()
    application[DB_KEY] = pool


async def close_app_database_pool(application: Application):
    print("Destroying database pool.")
    pool: Pool = application[DB_KEY]
    await pool.close()
