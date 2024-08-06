from aiohttp import web
from aiohttp.web_request import Request
from aiohttp.web_response import Response
from chapter_05.database import DB_KEY

cart_routes = web.RouteTableDef()


@cart_routes.get("/users/{id}/cart")
async def time(request: Request) -> Response:
    try:
        str_id = request.match_info["id"]
        user_id = int(str_id)
        db = request.app[DB_KEY]
        favorite_query = "SELECT product_id from user_cart where user_id = $1"
        result = await db.fetch(favorite_query, user_id)
        if result is not None:
            return web.json_response([dict(record) for record in result])
        else:
            raise web.HTTPNotFound()
    except ValueError:
        raise web.HTTPBadRequest()
