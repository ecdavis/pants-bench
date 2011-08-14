"""
A fake HTTP server using asyncore/asynchat.

For each \r\n\r\n-delimited string it receives, this server will send a
very short HTTP response. Useful for using HTTP benchmarking tools to
measure a framework's performance without involving the HTTP stack.
"""

import asynchat
import asyncore
import cProfile
import pstats
import socket

RESPONSE_DATA = "0123456789" * 2048
RESPONSE_LENGTH = len(RESPONSE_DATA)
RESPONSE = "HTTP/1.1 200 OK\r\nContent-Length: %d\r\n\r\n%s\r\n" % (RESPONSE_LENGTH, RESPONSE_DATA)

class RequestHandler(asynchat.async_chat):
    def __init__(self, sock):
        asynchat.async_chat.__init__(self, sock)
        self.set_terminator('\r\n\r\n')

    def collect_incoming_data(self, data):
        pass

    def found_terminator(self):
        self.push(RESPONSE)

class Server(asyncore.dispatcher):
    def __init__(self, host, port):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind((host, port))
        self.listen(1024)

    def handle_accept(self):
        while True:
            pair = self.accept()
            if pair is None:
                break
            else:
                sock, addr = pair
                handler = RequestHandler(sock)

server = Server('', 8080)
asyncore.loop(0.02, True)
