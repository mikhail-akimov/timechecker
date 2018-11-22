import socket
import time

sock = socket.socket()

sock.bind(("localhost", 8000))
sock.listen(socket.SOMAXCONN)
sock.settimeout(0.2)

clients = []

while True:
    print('Waiting for client')
    try:
        conn, addr = sock.accept()
        print('{} connected'.format(addr))
        clients.append(conn)
        print(clients)
    except socket.timeout:
        pass
    finally:
        while True:
            try:
                for client in clients:
                    try:
                        client.sendall(b'You are connected')
                    except ConnectionResetError:
                        clients.remove(client)
                        break
                    finally:
                        print('Sended....')
            except socket.timeout:
                break
            break
