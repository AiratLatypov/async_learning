import time
import requests
from concurrent.futures import ThreadPoolExecutor


def get_status_code(url: str) -> int:
    response = requests.get(url)
    return response.status_code


start_time = time.time()

with ThreadPoolExecutor() as pool:
    """
    Потоки дадут прирост в производительности в сравнении с синхронным вариантом, 
    но очень сильно проиграют варианту с aiohttp
    """
    urls = ["https://www.google.com/" for _ in range(1_000)]
    results = pool.map(get_status_code, urls)
    for result in results:
        print(result)

    end_time = time.time()

    print(f"Выполнение запросов завершено за {end_time - start_time:.4f} с")
    # Выполнение запросов завершено за 90.6803с
    # Выполнение запросов завершено за 79.7964с
