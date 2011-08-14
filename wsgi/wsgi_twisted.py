from twisted.internet import reactor
from twisted.web.server import Site
from twisted.web.wsgi import WSGIResource

from wsgi_app import application

site = Site(WSGIResource(reactor, reactor.getThreadPool(), application))
reactor.listenTCP(8080, site, 1024)
reactor.run()
