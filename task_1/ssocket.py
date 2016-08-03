import socket
import _thread
thread = _thread
import sys
import time

def operate(main_port):
    listen_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listen_s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listen_s.bind((HOST, main_port))
    listen_s.listen(1)
    s, addr = listen_s.accept()
    listen_s.close()
    print('Socket on port %d connected by %s' % (main_port, addr))
    thread.start_new_thread(writer, (s,))
    reader(s)

def reader(s):
    ch = s.recv(1)
    while ch:
        s.send(ch)
        ch = s.recv(1)
    s.close()

def writer(s):
    ch = sys.stdin.buffer.read(1)
    while ch:
        s.send(ch)
        ch = sys.stdin.buffer.read(1)

HOST = ''
if len(sys.argv) < 2:
    print("Usage: port")
else:
    main_port = int(sys.argv[1])
    operate(main_port)
