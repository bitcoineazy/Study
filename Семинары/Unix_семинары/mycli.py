#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

sock = socket.socket()
sock.connect(('localhost', 9090))

while True:
    word = input()
    sock.send(word.encode())
    data = sock.recv(1024).decode()
    if "EXIT" in data:
        sock.close()
        break
    print(data)
