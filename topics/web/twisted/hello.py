from twisted.internet import reactor
from twisted.web import resource, server


class HelloResource(resource.Resource):
    isLeaf = True
    numberRequests = 0

    def render_GET(self, request):
        self.numberRequests += 1
        request.setHeader("content-type", "text/plain")
        return "I am request #" + str(self.numberRequests) + "\n"


reactor.listenTCP(8082, server.Site(HelloResource()))
reactor.run()
