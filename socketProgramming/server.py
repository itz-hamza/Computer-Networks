import socket

HOST =  '192.168.56.1'
PORT = 9990

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind((HOST,PORT))

server.listen(5)

while True:
    c,a = server.accept()
    print(f"Connected to {a}")
    msg = c.recv(1024).decode('utf-8')
    print(f"the message from client is{msg}")
    c.send("recieved".encode('utf-8'))
    