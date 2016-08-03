import socket
import sys
import time
import _thread
thread = _thread


def operate(main_port, main_ip):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((main_ip, main_port))
    thread.start_new_thread(reader, (s,))
    writer(s)


def reader(s):
    ch = s.recv(1)
    while ch:
        sys.stdout.buffer.write(ch)
        sys.stdout.flush()
        ch = s.recv(1)


def writer(s):
    ch = sys.stdin.buffer.read(1)
    while ch:
        s.send(ch)
        ch = sys.stdin.buffer.read(1)

if len(sys.argv) < 3:
    print("Usage: ip port")
else:
    main_ip = sys.argv[1]
    main_port = int(sys.argv[2])
    operate(main_port, main_ip)
