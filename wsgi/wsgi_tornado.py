from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.wsgi import WSGIContainer

from wsgi_app import application

server = HTTPServer(WSGIContainer(application))
server.listen(8080)
IOLoop.instance().start()
