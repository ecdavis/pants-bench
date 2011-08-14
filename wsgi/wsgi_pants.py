from pants.contrib.http import HTTPServer
from pants.contrib.wsgi import WSGIConnector
from pants import engine

from wsgi_app import application

HTTPServer(WSGIConnector(application)).listen(8080)
engine.start()

