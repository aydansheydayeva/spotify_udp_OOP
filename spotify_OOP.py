import socket, argparse, random, sys
from datetime import datetime

class Server:
    MAX_BYTES = 65535

    def __init__(self, interface, port):
        self.interface = interface
        self.port = port
    
    def start(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind((self.interface, self.port))
        print(f"Server is listening at {sock.getsockname()}\n")

        while True:
            data, addr = sock.recvfrom(self.MAX_BYTES)
            
            if random.random() > 0.5:  # this part was added just to make an illusion of some packet dropping in case if client is able to connect but something went wrong with server and packets dropped
                print(f"Dropping data from {addr}")
                continue

            data = data.decode()
            print(f"Message from {addr}: {data}")
            message_to_send = f"Reply from Server: Data - {data} - was received"
            message_to_send.encode()
            sock.sendto(message_to_send.encode(), addr)
            print(f"server responded ...")


class Client:
    MAX_BYTES = 65535

    def __init__(self, hostname, port):
        self.hostname = hostname
        self.port = port
    
    def start(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        hostname = sys.argv[2]  # works without this as well
        sock.connect((self.hostname, self.port))
        print(f"Connected with Server at ({self.hostname}, {self.port})\n")

        delay = 0.1

        now = datetime.now()
        time1 = now.replace(hour = 12, minute = 0, second = 0, microsecond = 0)
        time2 = now.replace(hour = 17, minute = 0, second = 0, microsecond = 0)
        time3 = now.replace(hour = 23, minute = 59, second = 0, microsecond = 0)
        time4 = now.replace(hour = 0, minute = 0, second = 0, microsecond = 0)


        message = "This is from Client"
        response = ""
        message.encode()
        while True:
            sock.send(message.encode())
            print(f"waiting for response from SERVER for {delay} seconds")
            sock.settimeout(delay)

            try:
                response = sock.recv(self.MAX_BYTES)
            except socket.timeout:
                if (time1 <= now < time2 or now==time3 or time4 <= now <time1):
                    delay *= 2
                elif (time2 <= now < time3):
                    delay *=3

                if (time1 <= now < time2 and delay > 2) or (time2 <= now < time3 and delay >4) or ((now==time3 or time4 <= now <time1) and delay > 1):
                    raise RuntimeError('Server is probably down')
            else:
                break
        
        print(f"{response.decode()}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="UDP with exponential backoff ...")
    options={"client": Client, "server": Server}
    parser.add_argument("role", choices=options, help="SERVER or CLIENT")
    parser.add_argument("host", help="interface server listens at, hostname client sends to")
    parser.add_argument("-p", metavar="PORT", type=int, default=4444, help="UDP port (default 4444)")

    args=parser.parse_args()
    class_name = options[args.role]
    obj = class_name(args.host, args.p)
    obj.start()
