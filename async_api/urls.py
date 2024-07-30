from django.urls import path
from . import views

app_name = "async_api"

urlpatterns = [
    path("", views.requests_view, name="requests"),
    path("sync_to_async", views.sync_to_async_view),
    path("async_to_sync", views.requests_view_sync)
]

# command: gunicorn async_views.asgi:application -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
# http://localhost:8000/requests/?url=https://www.google.com/&request_num=10
# http://localhost:8000/requests/sync_to_async?sleep_time=5&num_calls=5&thread_sensitive=False
# http://localhost:8000/requests/async_to_sync?url=https://www.google.com/&request_num=10
