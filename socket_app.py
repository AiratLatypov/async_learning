import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # создаем TCP-сервер
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

address = ("127.0.0.1", 8000)  # задаем адрес сокета
server_socket.bind(address)
server_socket.listen()  # прослушиваем запросы на подключение, подключаемся через Putty
server_socket.setblocking(False)

connections = []

try:
    while True:
        try:
            connection, client_address = server_socket.accept()
            connection.setblocking(False)
            print(f"Получен запрос на подключение от {client_address}!")
            connections.append(connection)
        except BlockingIOError:
            pass

        for connection in connections:
            try:
                buffer = b""

                while buffer[-2:] != b"\r\n":
                    data = connection.recv(2)
                    if not data:
                        break
                    else:
                        print(f"Получены данные: {data}!")
                        buffer += data

                print(f"Все данные: {buffer}")
                connection.sendall(buffer)
            except BlockingIOError:
                pass
finally:
    server_socket.close()
