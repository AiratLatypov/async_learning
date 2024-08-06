from aiohttp import web
from aiohttp.web_request import Request
from aiohttp.web_response import Response
from chapter_05.database import DB_KEY

products_routes = web.RouteTableDef()


@products_routes.get("/products")
async def products(request: Request) -> Response:
    db = request.app[DB_KEY]
    product_query = "SELECT product_id, product_name FROM product"
    result = await db.fetch(product_query)
    return web.json_response([dict(record) for record in result])
