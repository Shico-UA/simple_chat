import sys
import socket
import time
from threading import Thread


def writer():
    s, addr = listen_s.accept()
    SOCKET_LIST.append(s)
    print("Client (%s, %s) connected" % addr)
    while 1:
        data = s.recv(1024)
        if not data:
            break
        print('Sending data back to clients')
        for socket in SOCKET_LIST:
            if socket != listen_s and socket != s:
                try:
                    socket.sendall(data)
                except:
                    socket.close()
                    print("Client (%s, %s) is offline" % addr)
                    if socket in SOCKET_LIST:
                        SOCKET_LIST.remove(socket)


if len(sys.argv) < 2:
    print("Usage: port")
else:
    HOST = ''
    SOCKET_LIST = []
    main_port = int(sys.argv[1])
    listen_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listen_s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listen_s.bind((HOST, main_port))
    listen_s.listen(2)
    for i in range(2):
        Thread(target=writer).start()
    listen_s.close()
