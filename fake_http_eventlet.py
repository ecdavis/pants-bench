"""
A fake HTTP server using eventlet.

For each \r\n\r\n-delimited string it receives, this server will send a
very short HTTP response. Useful for using HTTP benchmarking tools to
measure a framework's performance without involving the HTTP stack.
"""

import eventlet

def on_connect(sock):
    buf = ''
    while True:
        while '\r\n\r\n' not in buf:
            data = sock.readline()
            if not data:
                return
            buf += data
        sock.write("HTTP/1.1 200 OK\r\nContent-Length: 13\r\n\r\nHello, World!\r\n")
        sock.flush()

server = eventlet.listen(('', 8080))
pool = eventlet.GreenPool()
while True:
    try:
        sock, addr = server.accept()
        pool.spawn_n(on_connect, sock.makefile('rw'))
    except (SystemExit, KeyboardInterrupt):
        break
