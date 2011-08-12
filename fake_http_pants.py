"""
A fake HTTP server using Pants.

For each \r\n\r\n-delimited string it receives, this server will send a
very short HTTP response. Useful for using HTTP benchmarking tools to
measure a framework's performance without involving the HTTP stack.
"""

from pants import *

class FakeHTTP(Connection):
    def on_connect(self):
        self.read_delimiter = '\r\n\r\n'

    def on_read(self, data):
        self.write("HTTP/1.1 200 OK\r\nContent-Length: 13\r\n\r\nHello, World!\r\n")

Server(FakeHTTP).listen(8080)
engine.start()
