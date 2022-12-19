import socket
import os

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 12345))
str = "post file:setting"
client.send(str.encode("utf-8"))
data = client.recv(100).decode('utf-8')
if data.startswith("ok"):
    with open("setting.json", "rb") as f:
        client.sendfile(f)
client.close()
