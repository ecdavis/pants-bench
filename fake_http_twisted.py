"""
A fake HTTP server using Twisted.

For each \r\n\r\n-delimited string it receives, this server will send a
very short HTTP response. Useful for using HTTP benchmarking tools to
measure a framework's performance without involving the HTTP stack.
"""

from twisted.internet.protocol import Factory, Protocol
from twisted.internet import reactor

RESPONSE_DATA = "0123456789" * 2048
RESPONSE_LENGTH = len(RESPONSE_DATA)
RESPONSE = "HTTP/1.1 200 OK\r\nContent-Length: %d\r\n\r\n%s\r\n" % (RESPONSE_LENGTH, RESPONSE_DATA)

class FakeHTTP(Protocol):
    def connectionMade(self):
        self.buf = ''
    
    def dataReceived(self, data):
        self.buf += data
        if '\r\n\r\n' in self.buf:
            self.buf = ''
            self.transport.write(RESPONSE)

class FakeHTTPFactory(Factory):
    protocol = FakeHTTP

reactor.listenTCP(8080, FakeHTTPFactory(), 1024)
reactor.run()
