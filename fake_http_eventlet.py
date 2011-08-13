import eventlet

def on_connect(sock):
    buf = ''
    while True:
        while '\r\n\r\n' not in buf:
            data = sock.readline()
            if not data:
                return
            buf += data
        buf = buf[buf.find('\r\n\r\n')+4:]
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
