import socket
import argparse
import sys
import random
from datetime import datetime

class Server:
    MAX_BYTES=65535

    def __init__(self,interface,port):
        self.interface = interface
        self.port = port

    def connect(self):
        sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        sock.bind((self.interface,self.port))    
        print(f"Listening at {sock.getsockname()}")

        while True:
            data, address = sock.recvfrom(self.MAX_BYTES)
            if random.random() < 0.5: 
                print(f"Pretending to drop packet from {address}")
                continue
        
            text = data.decode("ascii")
            print(f"Client at {address} says {text}")

            server_text = f"Your data was {len(data)} bytes long"
            server_data = server_text.encode("ascii")
            sock.sendto(server_data,address)
            

class Client:
    MAX_BYTES=65535
    
    def __init__(self, hostname, port):
        self.hostname = hostname
        self.port = port
    

    def todayAt (self,hr, min=0, sec=0, micros=0):
        now = datetime.now()
        return now.replace(hour=hr, minute=min, second=sec, microsecond=micros)

    def connect(self):
        sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        hostname = sys.argv[2]
        sock.connect((self.hostname,self.port))
        print(f"Client socket name is {sock.getsockname()}")

        delay = 0.1
        text = f"This message sent at {datetime.now()}"
        data=text.encode("ascii")

        while True:
            sock.send(data)
            print(f"Waiting up to {delay} seconds for a reply from Server")
            sock.settimeout(delay)

            try:
                data = sock.recv(self.MAX_BYTES)
            except socket.timeout:
                TimeNow = datetime.now()
                if (TimeNow <= self.todayAt(12) and TimeNow <= self.todayAt(17)):
                    delay *= 2.0
                    if delay > 2.0:
                        raise RuntimeError("I think the server is down")

                elif ((TimeNow > self.todayAt(17)) and TimeNow <= self.todayAt(23,59)):
                    delay *= 3.0
                    if delay > 4.0:
                        raise RuntimeError("I think the server is down")
                
                else:
                    delay *= 2
                    if delay > 1.0:
                        raise RuntimeError("I think the server is down")
            else:
                break
        print(f"Server says {data.decode('ascii')}")
        
    
def main():
    choices = {"server":Server,"client":Client}
    parser = argparse.ArgumentParser()
    
    parser.add_argument("role",choices=choices,help="Client/Server")
    parser.add_argument("host",help="hostname client will send,interface server will listen to")
    parser.add_argument("-p",metavar="PORT",type=int,default=1060,help="Default port: 1060")

    args = parser.parse_args()
    cl = choices[args.role]
    instance = cl(args.host,args.p) #create class instance
    instance.connect()

if __name__ == "__main__":
    main()


        
        
            