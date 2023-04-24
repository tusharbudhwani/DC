import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect(('localhost', 3001))

sock.send('Hi, I am client and sent this data'.encode())

data = sock.recv(1024)
print(data.decode())

sock.close()