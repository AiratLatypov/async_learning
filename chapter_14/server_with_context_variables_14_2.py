import asyncio
from asyncio import StreamReader, StreamWriter
from contextvars import ContextVar


class Server:
    user_address = ContextVar("user_address")

    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port

    async def start_server(self):
        server = await asyncio.start_server(self._client_connected, self.host, self.port)
        await server.serve_forever()

    def _client_connected(self, reader: StreamReader, writer: StreamWriter):
        self.user_address.set(writer.get_extra_info("peername"))
        asyncio.create_task(self.listen_for_messages(reader))

    async def listen_for_messages(self, reader: StreamReader):
        while data := await reader.readline():
            print(f"Got message {data} from {self.user_address.get()}")


async def main():
    server = Server("127.0.0.1", 9000)
    await server.start_server()


asyncio.run(main())

# Got message b'GET / HTTP/1.1\r\n' from ('127.0.0.1', 50251)
# Got message b'Host: localhost:9000\r\n' from ('127.0.0.1', 50251)
# Got message b'Connection: keep-alive\r\n' from ('127.0.0.1', 50251)
# Got message b'sec-ch-ua: "Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"\r\n' from ('127.0.0.1', 50251)
# Got message b'sec-ch-ua-mobile: ?0\r\n' from ('127.0.0.1', 50251)
# Got message b'sec-ch-ua-platform: "Windows"\r\n' from ('127.0.0.1', 50251)
# Got message b'Upgrade-Insecure-Requests: 1\r\n' from ('127.0.0.1', 50251)
# Got message b'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36\r\n' from ('127.0.0.1', 50251)
# Got message b'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7\r\n' from ('127.0.0.1', 50251)
# Got message b'Sec-Fetch-Site: none\r\n' from ('127.0.0.1', 50251)
# Got message b'Sec-Fetch-Mode: navigate\r\n' from ('127.0.0.1', 50251)
# Got message b'Sec-Fetch-User: ?1\r\n' from ('127.0.0.1', 50251)
# Got message b'Sec-Fetch-Dest: document\r\n' from ('127.0.0.1', 50251)
# Got message b'Accept-Encoding: gzip, deflate, br, zstd\r\n' from ('127.0.0.1', 50251)
# Got message b'Accept-Language: ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,es;q=0.6\r\n' from ('127.0.0.1', 50251)
# Got message b'Cookie: PGADMIN_LANGUAGE=en; tabstyle=raw-tab; csrftoken=IRrv1WxDS4XfQnQ6yLNk4Ka8MOwtYXxw; sessionid=bv1tvucankqei53m8097nwt4n8kzl4wl\r\n' from ('127.0.0.1', 50251)
# Got message b'\r\n' from ('127.0.0.1', 50251)
