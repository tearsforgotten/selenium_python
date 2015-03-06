import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('192.168.1.239', 9874))
s.listen(5)

while True:
    conn, addr = s.accept()
    print("connected",  addr)

    while True:
        data = conn.recv(1024)
        if not data:
            break
        print("received: %s" % data)
        conn.send("%s" % data.upper())


    conn.close()

s.close()