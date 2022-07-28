import os
try:
    from socket import *
except ModuleNotFoundError:
    os.system("pip install socket")

serverName = "127.0.0.1"
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
message = ""
while message != b"q":
    message = bytes(input("Input lowercase sentence : "), encoding="utf8")
    clientSocket.sendto(message,(serverName,serverPort))
    modifiedMessage, serverAdress = clientSocket.recvfrom(2048)
    print(modifiedMessage)
clientSocket.close()