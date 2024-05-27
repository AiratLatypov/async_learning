import asyncio


async def delay(delay_seconds: int) -> int:
    print(f"Засыпаю на {delay_seconds} сек")
    await asyncio.sleep(delay_seconds)
    print(f"Сон в течение {delay_seconds} сек закончился")
    return delay_seconds
