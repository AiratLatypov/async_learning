import asyncio
import aiohttp
from aiohttp import ClientSession
from utils import async_timed


@async_timed()
async def fetch_status(session: ClientSession, url: str, delay: int = 0) -> int:
    await asyncio.sleep(delay)
    # ten_millis = aiohttp.ClientTimeout(total=10) timeout=ten_millis
    async with session.get(url) as result:
        return result.status


@async_timed()
async def main():
    session_timeout = aiohttp.ClientTimeout(total=1, connect=.1)
    async with aiohttp.ClientSession(timeout=session_timeout) as session:
        url = "https://google.com"
        status = await fetch_status(session, url)
        print(f"Состояние для {url} было равно {status}")


# asyncio.run(main())
