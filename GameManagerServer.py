import socket
import os
import hashlib


def TransFile():
    server = socket.socket()
    server.bind(("localhost", 12345))
    server.listen()
    while True:
        new_sock, addr = server.accept()
        data = new_sock.recv(1024)
        data = data.decode("utf-8")
        if data.startswith("get file"):
            with open("setting.json", "rb") as f:
                new_sock.sendfile(f)
        elif data.startswith("post file"):
            str = "ok"
            new_sock.send(str.encode('utf-8'))
            with open("setting.json", "wb") as f:
                file_data = new_sock.recv(1024)
                f.write(file_data)


if __name__ == "__main__":
    TransFile()
   