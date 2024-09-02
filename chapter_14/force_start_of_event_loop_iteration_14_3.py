import asyncio


async def delay(delay_seconds: int) -> int:
    print(f"Засыпаю на {delay_seconds} сек")
    await asyncio.sleep(delay_seconds)
    print(f"Сон в течение {delay_seconds} сек закончился")
    return delay_seconds


async def create_tasks_no_sleep():
    task1 = asyncio.create_task(delay(1))
    task2 = asyncio.create_task(delay(2))
    print("Gathering tasks:")
    await asyncio.gather(task1, task2)


async def create_tasks_sleep():
    """Запуск задач сразу после их создания. Может быть полезно для долгих задач, чтобы избежать блокировки цикла
    событий."""
    task1 = asyncio.create_task(delay(1))
    await asyncio.sleep(0)
    task2 = asyncio.create_task(delay(2))
    await asyncio.sleep(0)
    print("Gathering tasks:")
    await asyncio.gather(task1, task2)


async def main():
    print("--- Testing without asyncio.sleep(0) ---")
    await create_tasks_no_sleep()
    print("--- Testing with asyncio.sleep(0) ---")
    await create_tasks_sleep()

asyncio.run(main())

# --- Testing without asyncio.sleep(0) ---
# Gathering tasks:
# Засыпаю на 1 сек
# Засыпаю на 2 сек
# Сон в течение 1 сек закончился
# Сон в течение 2 сек закончился
# --- Testing with asyncio.sleep(0) ---
# Засыпаю на 1 сек
# Засыпаю на 2 сек
# Gathering tasks:
# Сон в течение 1 сек закончился
# Сон в течение 2 сек закончился
