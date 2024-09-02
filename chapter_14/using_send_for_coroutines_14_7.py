async def say_hello():
    print("Hello!")


async def say_goodbye():
    print("Goodbye!")


async def meet_and_greet():
    await say_hello()
    await say_goodbye()


coro = meet_and_greet()

coro.send(None)

# Hello!
# Goodbye!
# Traceback (most recent call last):
#   File "F:\python_projects\async_learning\chapter_14\using_send_for_coroutines_14_7.py", line 16, in <module>
#     coro.send(None)
# StopIteration
