from aiohttp import web

from chapter_05.database import add_database_pool_to_app, close_app_database_pool
from chapter_09.rest_api_with_aiohttp.endpoint_to_return_time_9_1 import time_route
from chapter_09.rest_api_with_aiohttp.connection_to_db_9_2 import routes_brands_list
from chapter_09.rest_api_with_aiohttp.good_detail_9_3 import product_detail_route
from chapter_09.rest_api_with_aiohttp.good_creating_9_4 import product_create_route


app = web.Application()
app.on_startup.append(add_database_pool_to_app)
app.on_cleanup.append(close_app_database_pool)

app.add_routes(time_route)
app.add_routes(routes_brands_list)
app.add_routes(product_detail_route)
app.add_routes(product_create_route)


if __name__ == "__main__":
    web.run_app(app, host="0.0.0.0", port=8080)
