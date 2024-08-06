from aiohttp import web

from chapter_05.database import add_database_pool_to_app, close_app_database_pool
from chapter_10.microservices.stock_availability_service_10_1 import inventory_routes
from chapter_10.microservices.favorites_service_10_5 import favorites_routes
from chapter_10.microservices.cart_service_10_6 import cart_routes
from chapter_10.microservices.products_service_10_7 import products_routes
from chapter_10.microservices.backend_for_frontend_products_10_8 import all_products_routes


app = web.Application()
app.on_startup.append(add_database_pool_to_app)
app.on_cleanup.append(close_app_database_pool)

app.add_routes(inventory_routes)
app.add_routes(favorites_routes)
app.add_routes(cart_routes)
app.add_routes(products_routes)
app.add_routes(all_products_routes)


if __name__ == "__main__":
    web.run_app(app, host="0.0.0.0", port=8001)