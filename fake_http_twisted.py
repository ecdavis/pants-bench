"""
A fake HTTP server using Twisted.

For each \r\n\r\n-delimited string it receives, this server will send a
very short HTTP response. Useful for using HTTP benchmarking tools to
measure a framework's performance without involving the HTTP stack.
"""

from twisted.internet.protocol import Factory, Protocol
from twisted.internet import reactor

class FakeHTTP(Protocol):
    def connectionMade(self):
        self.buf = ''
    
    def dataReceived(self, data):
        self.buf += data
        mark = self.buf.find('\r\n\r\n')
        if mark != -1:
            self.buf = self.buf[mark+4:]
        self.transport.write("HTTP/1.1 200 OK\r\nContent-Length: 13\r\n\r\nHello, World!\r\n")

class FakeHTTPFactory(Factory):
    protocol = FakeHTTP

reactor.listenTCP(8080, PlainFactory(), 1024)
reactor.run()
