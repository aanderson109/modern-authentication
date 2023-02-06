import socket
import threading

# information about connections
connections = []
total_connections = 0

'''
Client Class
creates new instance for each client connected to the server
'''
class Client(threading.Thread):
    def __init__(self, socket, address, id, name, signal):
        threading.Thread.__init__(self)
        self.socket = socket
        self.address = address
        self.id = id
        self.name = name
        self.signal = signal
    
    def __str__(self):
        return str(self.id) + " " + str(self.address)   # needs less clunky formatting
    
    def run(self):
        '''
        Method that attempts to get data from client
            IF NO DATA RECEIVED --> assume client disconnected, remove from server
            IF DATA IS RECEIVED --> print data, send data to all other connected clients
        '''
        while self.signal:
            try:
                data = self.socket.recv(32)
            except:
                print("---------------------------------------------------\n")
                print("Client | " + str(self.address) + " | DISCONNECTED |\n")
                print("---------------------------------------------------\n")
                self.signal = False
                connections.remove(self)
                break
            if data != "":
                print("---------------------------------------------------\n")
                print("ID | " + str(self.id) + " | " + str(data.decode("utf-8")) + " | ")
                print("---------------------------------------------------\n")
                for client in connections:
                    if client.id != self.id:
                        client.socket.sendall(data)

def newConnections(socket):
    '''
    waits for new connections
    '''
    while True:
        sock, address = socket.accept()
        global total_connections
        connections.append(Client(sock, address, total_connections, "name", True))
        connections[len(connections) - 1].start()
        print("new connection --> " + str(connections[len(connections) - 1]))
        total_connections += 1

def main():
    '''
    main method to run
    '''
    # get host, port
    host = input("host --> ")
    port = int(input("port --> "))

    # create new server socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((host, port))
    sock.listen(5)

    # create new thread, wait for connections
    newConnectionsThread = threading.Thread(target = newConnections, args = (sock,))
    newConnectionsThread.start()

main()
