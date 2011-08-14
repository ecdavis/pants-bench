from twisted.internet import reactor
from twisted.web import server, resource

RESPONSE_DATA = "0123456789" * 1

class Simple(resource.Resource):
    isLeaf = True
    def render_GET(self, request):
        return RESPONSE_DATA

site = server.Site(Simple())
reactor.listenTCP(8080, site)
reactor.run()
