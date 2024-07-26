from aiohttp import web
from aiohttp.web_request import Request
from aiohttp.web_response import Response
from asyncpg import Record
from asyncpg.pool import Pool

from chapter_05.database import DB_KEY

product_detail_route = web.RouteTableDef()


@product_detail_route.get("/products/{id}")
async def get_product(request: Request) -> Response:
    try:
        str_id = request.match_info["id"]
        product_id = int(str_id)

        query = \
            """
            SELECT
            product_id,
            product_name,
            brand_id
            FROM product
            WHERE product_id = $1
            """

        connection: Pool = request.app[DB_KEY]
        result: Record = await connection.fetchrow(query, product_id)
        print("RESULT", result)

        if result is not None:
            return web.json_response(dict(result))
        else:
            raise web.HTTPNotFound()
    except ValueError:
        raise web.HTTPBadRequest()
