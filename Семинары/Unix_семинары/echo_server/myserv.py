#!/usr/bin/env python
 
import socket
import os
 
sock = socket.socket()
server_address = ('', 9090)
sock.bind(('', 9090))
print(f'Старт сервера на localhost порт {server_address[1]}')
sock.listen(1)
print('Ожидаем соединения')
conn, addr = sock.accept()
print(f'Соединение с {addr} установлено')

while True: 
    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        conn.send(data.upper().encode())
        if "exit".lower() in data:
            conn.close()
            os._exit(0)
