import asyncio
import random
from aiohttp import web
from aiohttp.web_request import Request
from aiohttp.web_response import Response

inventory_routes = web.RouteTableDef()


@inventory_routes.get("/products/{id}/inventory")
async def get_inventory(request: Request) -> Response:
    delay: float = random.randint(0, 20) / 10
    await asyncio.sleep(delay)
    inventory: int = random.randint(0, 100)
    return web.json_response({"inventory": inventory})
