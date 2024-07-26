from asyncpg import Record
from asyncpg.pool import Pool
from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import JSONResponse, Response
from starlette.routing import Route

from chapter_05.database import create_pool


async def create_database_pool():
    pool: Pool = await create_pool()
    app.state.DB = pool


async def destroy_database_pool():
    pool = app.state.DB
    await pool.close()


async def brands(request: Request) -> Response:
    connection: Pool = request.app.state.DB
    brand_query = "SELECT brand_id, brand_name FROM brand"
    results: list[Record] = await connection.fetch(brand_query)
    result_as_dict: list[dict] = [dict(brand) for brand in results]
    return JSONResponse(result_as_dict)


app = Starlette(
    routes=[Route("/brands", brands)],
    on_startup=[create_database_pool],
    on_shutdown=[destroy_database_pool]
)

# command to start: uvicorn --workers 8 --log-level error chapter_09.starlette.brands_api_9_8:app
