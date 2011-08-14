"""
A fake HTTP server using eventlet.

For each \r\n\r\n-delimited string it receives, this server will send a
very short HTTP response. Useful for using HTTP benchmarking tools to
measure a framework's performance without involving the HTTP stack.
"""

import eventlet

RESPONSE_DATA = "0123456789" * 1
RESPONSE_LENGTH = len(RESPONSE_DATA)
RESPONSE = "HTTP/1.1 200 OK\r\nContent-Length: %d\r\n\r\n%s" % (RESPONSE_LENGTH, RESPONSE_DATA)

def on_connect(sock):
    buf = ''
    while True:
        while '\r\n\r\n' not in buf:
            data = sock.recv(4096)
            if not data:
                return sock.close()
            buf += data
        buf = ''
        try:
            sock.sendall(RESPONSE)
        except:
            return sock.close()

server = eventlet.listen(('', 8080))
pool = eventlet.GreenPool()
while True:
    try:
        sock, addr = server.accept()
        pool.spawn_n(on_connect, sock)
    except (SystemExit, KeyboardInterrupt):
        break
