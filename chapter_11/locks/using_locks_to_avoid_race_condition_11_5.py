import asyncio
from asyncio import Lock


class MockSocket:
    def __init__(self):
        self.socket_closed = False

    async def send(self, msg: str):
        if self.socket_closed:
            raise Exception("Socket is closed!")
        print(f"Sending: {msg}")
        await asyncio.sleep(1)
        print(f"Sent: {msg}")

    def close(self):
        self.socket_closed = True


user_names_to_sockets = {
    "John": MockSocket(),
    "Terry": MockSocket(),
    "Graham": MockSocket(),
    "Eric": MockSocket(),
}


async def user_disconnect(username: str, user_lock: Lock):
    print(f"{username} disconnected!")
    async with user_lock:
        print(f"Removing {username} from dictionary")
        socket = user_names_to_sockets.pop(username)
        socket.close()


async def message_all_users(user_lock: Lock):
    print("Creating message tasks")
    async with user_lock:
        messages = [
            socket.send(f"Hello {user}")
            for user, socket
            in user_names_to_sockets.items()
        ]
        await asyncio.gather(*messages)


async def main():
    """
    Поскольку message_all_users захватывает блокировку раньше, то функции user_disconnect приходится дожидаться
    ее освобождения. Это дает возможность окончить рассылку до отключения.
    """
    user_lock = Lock()
    await asyncio.gather(
        message_all_users(user_lock),
        user_disconnect("Eric", user_lock),
    )


asyncio.run(main())

# Output:
# Creating message tasks
# Eric disconnected!
# Sending: Hello John
# Sending: Hello Terry
# Sending: Hello Graham
# Sending: Hello Eric | !!!
# Sent: Hello John
# Sent: Hello Graham
# Sent: Hello Terry
# Sent: Hello Eric
# Removing Eric from dictionary
