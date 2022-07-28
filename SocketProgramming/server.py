import os
try:
    from socket import *
except ModuleNotFoundError:
    os.system("pip install socket")

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(("127.0.0.1", serverPort))
print("the server is ready to receive")

while 1:
    message, clientAddress = serverSocket.recvfrom(2028)
    print(f"{clientAddress}'den gelen mesaj : {message}")
    modifiedMessage = message.upper()
    print(f"{clientAddress}'a gönderilen mesaj : {modifiedMessage}")

    serverSocket.sendto(modifiedMessage, clientAddress)

# Run "python server.py" in one terminal and then run "python client.py" on another terminal same time
# in client.py terminal window enter message
# the message will sent to server and then modified as uppercase and then send back to client.