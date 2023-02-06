import socket
import threading
import sys

# wait for data sent from server
def receive(socket, signal):
    while signal:
        try:
            data = socket.recv(32)
            print(str(data.decode("utf-8")))    # data.decode used to turn message from bytes to a string
        except:
            print("DISCONNECTED")
            signal = False
            break

# get host, port
host = input("host --> ")
port = int(input("port --> "))

# attempt to connect to the server
try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
except:
    print("connection failed")
    print("\nGoodbye!")
    sys.exit(0)

# create new thread to wait for data
receiveThread = threading.Thread(target = receive, args = (sock, True))
receiveThread.start()

# send data to server
while True:
    message = input()
    sock.sendall(str.encode(message))   # used to turn string into bytes
