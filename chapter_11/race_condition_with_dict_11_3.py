import asyncio


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


async def user_disconnect(username: str):
    print(f"{username} disconnected!")
    socket = user_names_to_sockets.pop(username)
    socket.close()


async def message_all_users():
    print("Creating message tasks")
    messages = [
        socket.send(f"Hello {user}")
        for user, socket
        in user_names_to_sockets.items()
    ]
    await asyncio.gather(*messages)


async def main():
    """
    Ключевое различие между ошибками многопоточной и однопоточной конкурентности заключается в том, что в
    многопоточном приложении состояние гонки возможны везде, где модифицируется разделяемое состояние. А в
    модели однопоточной конкурентности нужно модифицировать состояние в точке await.
    """

    await asyncio.gather(message_all_users(), user_disconnect("Eric"))


asyncio.run(main())

# Output
# Creating message tasks
# Eric disconnected!
# Sending: Hello John
# Sending: Hello Terry
# Sending: Hello Graham
# raise Exception("Socket is closed!")
# Exception: Socket is closed!
