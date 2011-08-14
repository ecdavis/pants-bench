from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop

RESPONSE_DATA = "0123456789" * 1
RESPONSE_LENGTH = len(RESPONSE_DATA)
RESPONSE = "HTTP/1.1 200 OK\r\nContent-Length: %d\r\n\r\n%s" % (RESPONSE_LENGTH, RESPONSE_DATA)

def request_handler(request):
    request.write(RESPONSE)
    request.finish()

HTTPServer(request_handler).listen(8080)
IOLoop.instance().start()
