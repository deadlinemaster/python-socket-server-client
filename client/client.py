import socket
# 1
HOST = "192.168.1.45"
PORT = 777
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.sendall('111')
data = s.recv(1024)
s.close()
print(data)
