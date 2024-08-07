import asyncio
from chapter_10.circuit_breaker.simple_breaker_10_11 import CircuitBreaker


async def main():
    async def slow_callback():
        await asyncio.sleep(2)

    cb = CircuitBreaker(
        slow_callback,
        timeout=1.0,
        time_window=5,
        max_failures=2,
        reset_interval=5,
    )

    for _ in range(4):
        try:
            await cb.request()
        except Exception as e:
            pass

    print("Sleeping for 5 seconds so breaker closes...")
    await asyncio.sleep(5)

    for _ in range(4):
        try:
            await cb.request()
        except Exception as e:
            pass


asyncio.run(main())

# Output:
# app-1  | Circuit is closed, requesting!
# app-1  | Making request!
# app-1  | Circuit is closed, requesting!
# app-1  | Making request!
# app-1  | Circuit is open, failing fast!
# app-1  | Circuit is open, failing fast!
# app-1  | Sleeping for 5 seconds so breaker closes...
# app-1  | Circuit is going from open to closed, resetting!
# app-1  | Making request!
# app-1  | Circuit is closed, requesting!
# app-1  | Making request!
# app-1  | Circuit is open, failing fast!
# app-1  | Circuit is open, failing fast!
