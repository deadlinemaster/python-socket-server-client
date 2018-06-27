import socket

def getHtml():
    f = open("form.html", "r")
    sHtml = f.read()
    f.close()
    return sHtml

HOST = "192.168.1.45"
PORT = 81
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

while 1:

    try:
        sStatus = "HTTP/1.1 200 OK\r\n"
        sStatus += "\r\n"
        sStatus += getHtml()

        conn, addr = s.accept()
        print('Connection received', addr)
        data = conn.recv(65535)
        print(data)
        conn.sendall(sStatus)
        print('Connection closed')
        conn.close()

    except KeyboardInterrupt:
        print("111111111111Ctr+C")
        s.close()