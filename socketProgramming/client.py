import socket

HOST =  '192.168.56.1'
PORT = 9990

socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket.connect((HOST,PORT))

socket.send("Hello world".encode('utf-8'))
print(socket.recv(1024).decode('utf-8'))