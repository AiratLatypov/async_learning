import asyncio
import logging
import socket
from asyncio import AbstractEventLoop


async def echo(connection: socket, loop: AbstractEventLoop) -> None:
    try:
        while data := await loop.sock_recv(connection, 1024):  # В бесконечном цикле ожидаем данных от клиента
            print(f"Получены данные! {data}")
            if data == b"boom":
                raise Exception("Неожиданная ошибка сети")
            await loop.sock_sendall(connection, data)  # Получив данные отправляем их обратно клиенту
    except Exception as ex:
        logging.exception(ex)
    finally:
        connection.close()


async def listen_for_connections(server_socket: socket, loop: AbstractEventLoop):
    while True:
        connection, address = await loop.sock_accept(server_socket)
        connection.setblocking(False)
        print(f"Получен запрос на подключение от {address}")
        # После получения запроса на подключение создаем задачу echo, ожидающую данные от клиента
        asyncio.create_task(echo(connection, loop))


async def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server_address = ("127.0.0.1", 8000)
    server_socket.setblocking(False)
    server_socket.bind(server_address)
    server_socket.listen()

    # Запускаем сопрограмму прослушивания порта на предмет подключений
    await listen_for_connections(server_socket, asyncio.get_event_loop())

asyncio.run(main())
