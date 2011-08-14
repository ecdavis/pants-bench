from eventlet import listen
from eventlet.wsgi import server

from wsgi_app import application

server(listen(('', 8080), backlog=1024), application, max_size=8096)
