from datetime import datetime

from aiohttp import web
from aiohttp.web_request import Request
from aiohttp.web_response import Response

time_route = web.RouteTableDef()


@time_route.get("/time")
async def time(request: Request) -> Response:
    print("REQUEST", request.__dict__)
    today = datetime.today()

    result = {
        "month": today.month,
        "day": today.day,
        "time": str(today.time())
    }

    return web.json_response(result)
