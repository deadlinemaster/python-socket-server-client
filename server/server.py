# -*- coding: utf-8 -*-

import socket

class Server:

    HOST = ""

    # если порт указать меньше 1024, система запросит права суперпользователя
    PORT = 8081
    filename = "form.html"

    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((self.HOST, self.PORT))


    def listen(self):
        self.socket.listen(1)
        while 1:

            try:
                conn, addr = self.socket.accept()
                print('Connection received', addr)

                data = conn.recv(65535)
                print(data)

                response = self.getResponse()
                conn.sendall(response)

                conn.close()
                print('Connection closed')

            except KeyboardInterrupt:
                print("Ctr+C ---> stop server")
                self.socket.close()


    def getResponse(self):
        sStatus = "HTTP/1.1 200 OK\r\n"
        sStatus += "\r\n"
        sStatus += self.getHtml()

        return sStatus


    def getHtml(self):

        fd = open(self.filename, "r")
        html = fd.read()
        fd.close()

        return html