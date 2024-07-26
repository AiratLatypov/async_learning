import asyncpg
import os

from asyncpg import Pool
from aiohttp.web_app import Application

DB_KEY = "database"
DB_NAME = os.getenv("DATABASE_NAME")
DB_HOST = os.getenv("DATABASE_HOST")
DB_USER = os.getenv("DATABASE_USER")
DB_PORT = os.getenv("DATABASE_PORT")
DB_PASS = os.getenv("DATABASE_PASSWORD")
DB_PRODUCTS_NAME = os.getenv("PRODUCTS_DB_NAME")


async def create_connection():
    connection = await asyncpg.connect(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASS,
        database=DB_PRODUCTS_NAME,
    )
    return connection


async def create_pool(min_size=6, max_size=6) -> Pool:
    pool: Pool = await asyncpg.create_pool(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASS,
        database=DB_PRODUCTS_NAME,
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
