import socket
import pickle

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = socket.gethostname() 
        self.port = 5555    
        self.addr = (self.server, self.port)   
        self.id = self.connect() #connection id

    def getPlayer(self):
        return self.id

    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(2048).decode()
        except:
            pass
    
    def send(self, data):
        try:
            self.client.send(pickle.dumps(data))
            return pickle.loads(self.client.recv(2048*2))
        except socket.error as e:
            print(e)


    def disconnect(self):
        try:
            self.client.shutdown(4)
            self.client.close()
        except:
            pass