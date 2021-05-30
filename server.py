import socket
import threading

    


class ChatServer:

    clients_list = []
    americano = 30
    waffle = 30
    latte = 30
    smoothie=30
    coldbrew=30
    espresso=30
    prafe=30
    last_received_message = ""

    def __init__(self, americano = 30, waffle = 30, latte = 30,smoothie=30,coldbrew=30,espresso=30,prafe=30):
        
        self.create_listening_server()
        self.americano = americano
        self.waffle = waffle
        self.latte = latte
        self.smoothie=30
        self.coldbrew=30
        self.espresso=30
        self.prafe=30

    def update(self, menu, n,senders_socket):
        print('update', menu, n)
        if menu == "americano":
            if self.americano>0:
                self.americano -= int(n)
                if self.americano == 0:
                    text="Now "+menu+" is sold out!"
                    for client in self.clients_list:
                        socket, (ip, port) = client
                        socket.sendall(text.encode('utf-8'))
            
        elif menu == "latte":
            if self.latte>0:
                self.latte -= int(n)
                if self.latte == 0:
                    text="Sorry,"+menu+" is sold out!"
                    for client in self.clients_list:
                        socket, (ip, port) = client
                        socket.sendall(text.encode('utf-8'))
        elif menu == "waffle":
            if self.waffle>0:
                self.waffle -= int(n)
                if self.waffle == 0:
                    text="Sorry,"+menu+" is sold out!"
                    for client in self.clients_list:
                        socket, (ip, port) = client
                        socket.sendall(text.encode('utf-8'))
        elif menu == "smoothie":
            if self.smoothie>0:
                self.smoothie -= int(n)
                if self.smoothie == 0:
                    text="Sorry,"+menu+" is sold out!"
                    for client in self.clients_list:
                        socket, (ip, port) = client
                        socket.sendall(text.encode('utf-8'))
        elif menu == "espresso":
            if self.espresso>0:
                self.espresso -= int(n)
                if self.espresso == 0:
                    text="Sorry,"+menu+" is sold out!"
                    for client in self.clients_list:
                        socket, (ip, port) = client
                        socket.sendall(text.encode('utf-8'))
        elif menu == "coldbrew":
            if self.coldbrew>0:
                self.coldbrew -= int(n)
                if self.coldbrew == 0:
                    text="Sorry,"+menu+" is sold out!"
                    for client in self.clients_list:
                        socket, (ip, port) = client
                        socket.sendall(text.encode('utf-8'))
        elif menu == "prafe":
            if self.prafe>0:
                self.prafe -= int(n)
                if self.prafe == 0:
                    text="Sorry,"+menu+" is sold out!"
                    for client in self.clients_list:
                        socket, (ip, port) = client
                        socket.sendall(text.encode('utf-8'))

    def create_listening_server(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        local_ip = '220.66.218.156'
        local_port = 50005
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((local_ip, local_port))
        print("Listening for incoming messages..")
        self.server_socket.listen(5)
        self.receive_messages_in_a_new_thread()

    def receive_messages(self, so):
        while True:
            incoming_buffer = so.recv(256)
            if not incoming_buffer:
                break
            
            self.last_received_message = incoming_buffer.decode('utf-8')
            
            user, t = map(str, self.last_received_message.split(':'))
            menu, n = map(str, t.split())
            
            self.update(menu, n,so)
            self.send_numbers(so)
            
        so.close()
    def send_numbers(self,senders_socket):
        text=" "+str(self.americano)+" "+str(self.latte)+" "+str(self.waffle)+" "+str(self.smoothie)+" "+str(self.coldbrew)+" "+str(self.espresso)+" "+str(self.prafe)
        for client in self.clients_list:
            socket,(ip,port)=client
            socket.sendall(text.encode('utf-8'))
    def broadcast_to_all_clients(self, senders_socket):
        for client in self.clients_list:
            socket, (ip, port) = client
            if socket is not senders_socket:
                
                socket.sendall(self.last_received_message.encode('utf-8'))
                
                
                

    def receive_messages_in_a_new_thread(self):
        while 1:
            client = so, (ip, port) = self.server_socket.accept()
            self.add_to_clients_list(client)
            print ('Connected to ', ip, ':', str(port))
            self.broadcast_to_all_clients(so)

            t = threading.Thread(target=self.receive_messages, args=(so,))
            t.start()


    def add_to_clients_list(self, client):
        if client not in self.clients_list:
            self.clients_list.append(client)

if __name__ == "__main__":
    ChatServer()