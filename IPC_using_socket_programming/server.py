# For Server
# First import socket,
# create socket
# bind to IP and port
# start listening for connection requests
# Accept connection req
# Send encoded message
# Receive received message via connection
# decode and print it
# close the connection



# For client
# import socket
# create socket
# connect to the IP and port
# receive data
# decode and print data
# send encoded data
# close sock








import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.bind(('localhost', 3001))

sock.listen(1)
conn, addr = sock.accept()

data = conn.recv(1024)
print(data.decode())

conn.send("Hi, I am a server and sent this message".encode())

conn.close()





















