from asyncpg import Record
from asyncpg.pool import Pool

from aiohttp import web
from aiohttp.web_request import Request
from aiohttp.web_response import Response

from chapter_05.database import DB_KEY

routes_brands_list = web.RouteTableDef()


@routes_brands_list.get("/brands")
async def brands(request: Request) -> Response:
    connection: Pool = request.app[DB_KEY]
    brand_query = "SELECT brand_id, brand_name FROM brand"
    results: list[Record] = await connection.fetch(brand_query)
    result_as_dict: list[dict] = [dict(brand) for brand in results]
    return web.json_response(result_as_dict)
