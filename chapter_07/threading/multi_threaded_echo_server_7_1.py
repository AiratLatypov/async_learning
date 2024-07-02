import socket
from threading import Thread


def echo(client: socket):
    while True:
        data = client.recv(2048)
        print(f"Получено {data}, отправляю!")
        client.sendall(data)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(("127.0.0.1", 8080))
    server.listen()

    while True:
        connection, _ = server.accept()  # блокируется в ожидании клиентов
        thread = Thread(target=echo, args=(connection,))  # создаем поток, как только клиент подключился
        thread.start()
