import socket
import threading
from threading import Thread, Lock

    


class Server:
    # 연결된 클라이언트 정보 저장하는 리스트
    clients_list = []
    
    # 재고 초기값 ( GUI 구현 위함 )
    americano = 30
    waffle = 30
    latte = 30
    smoothie=30
    coldbrew=30
    espresso=30
    prafe=30
    lock = threading.Lock()
    last_received_info = ""
    
    def __init__(self, americano = 30, waffle = 30, latte = 30,smoothie=30,coldbrew=30,espresso=30,prafe=30):
        #lock = threading.Lock()
        self.create_listening_server()
        self.americano = americano
        self.waffle = waffle
        self.latte = latte
        self.smoothie= smoothie
        self.coldbrew= coldbrew
        self.espresso= espresso
        self.prafe= prafe

    # 재고 변경 함수 menu : 메뉴이름, n : 변경 개수
    def update(self, menu, n):
        
        if menu == "americano":
            if self.americano>0: # 아메리카노 재고 있으면 
                self.americano -= int(n) # 하나를 뺌
                if self.americano == 0: # 하나 빼고 난 후 재고 없으면
                    text="Now "+menu+" is sold out!" # 품절 메시지
                    for client in self.clients_list: # 모든 클라이언트에게 품절되었음을 알림
                        socket, (ip, port) = client
                        with self.lock:
                            socket.sendall(text.encode('utf-8'))
            
        elif menu == "latte":
            if self.latte>0:
                self.latte -= int(n)
                if self.latte == 0:
                    text="Sorry,"+menu+" is sold out!"
                    for client in self.clients_list:
                        socket, (ip, port) = client
                        with self.lock:
                            socket.sendall(text.encode('utf-8'))
        elif menu == "waffle":
            if self.waffle>0:
                self.waffle -= int(n)
                if self.waffle == 0:
                    text="Sorry,"+menu+" is sold out!"
                    for client in self.clients_list:
                        socket, (ip, port) = client
                        with self.lock:
                            socket.sendall(text.encode('utf-8'))
        elif menu == "smoothie":
            if self.smoothie>0:
                self.smoothie -= int(n)
                if self.smoothie == 0:
                    text="Sorry,"+menu+" is sold out!"
                    for client in self.clients_list:
                        socket, (ip, port) = client
                        with self.lock:
                            socket.sendall(text.encode('utf-8'))
        elif menu == "espresso":
            if self.espresso>0:
                self.espresso -= int(n)
                if self.espresso == 0:
                    text="Sorry,"+menu+" is sold out!"
                    for client in self.clients_list:
                        socket, (ip, port) = client
                        with self.lock:
                            socket.sendall(text.encode('utf-8'))
        elif menu == "coldbrew":
            if self.coldbrew>0:
                self.coldbrew -= int(n)
                if self.coldbrew == 0:
                    text="Sorry,"+menu+" is sold out!"
                    for client in self.clients_list:
                        socket, (ip, port) = client
                        with self.lock:
                            socket.sendall(text.encode('utf-8'))
        elif menu == "prafe":
            if self.prafe>0:
                self.prafe -= int(n)
                if self.prafe == 0:
                    text="Sorry,"+menu+" is sold out!"
                    for client in self.clients_list:
                        socket, (ip, port) = client
                        with self.lock:
                            socket.sendall(text.encode('utf-8'))

    # 서버 소켓 생성
    def create_listening_server(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # 소켓 생성
        local_ip = '192.168.1.9' # 서버 ip
        local_port = 50005 # 포트 번호
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
        self.server_socket.bind((local_ip, local_port))
        print("Listening for connect..")
        self.server_socket.listen(5) # 최대 5개 소켓 연결 가능
        self.receive_info_in_a_new_thread()

    # 클라이언트로부터 메시지 받음
    def receive_info(self, so):
        while True:
            incoming_buffer = so.recv(256)
            if not incoming_buffer:
                break
            
            # 클라이언트로 받은 문자 decoding
            self.last_received_info = incoming_buffer.decode('utf-8')
            
            # 문자 parsing(user이름, 메뉴이름, 변경 개수)
            user, t = map(str, self.last_received_info.split(':'))
            menu, n = map(str, t.split())
            
            # 메뉴 변경
            self.update(menu, n)
            # 클라이언트에게 재고 변경 알림
            self.send_numbers()
            
        so.close()
    # 클라이언트에 재고 보냄 (아메리카노 와플 스무디 콜드브루 에스프레소 프라페)
    def send_numbers(self):
        text=" "+str(self.americano)+" "+str(self.latte)+" "+str(self.waffle)+" "+str(self.smoothie)+" "+str(self.coldbrew)+" "+str(self.espresso)+" "+str(self.prafe)
        for client in self.clients_list:
            socket,(ip,port)=client
            socket.sendall(text.encode('utf-8'))

    # 다른 클라이언트들에게 정보 보냄
    def broadcast_to_all_clients(self, senders_socket):
        for client in self.clients_list:
            socket, (ip, port) = client
            if socket is not senders_socket:
                socket.sendall(self.last_received_info.encode('utf-8'))
                
    # 클라이언트와 소켓 연결
    def receive_info_in_a_new_thread(self):
        while 1:
            # accept
            client = so, (ip, port) = self.server_socket.accept()
            # 클라이언트 목록에 추가
            self.add_to_clients_list(client)
            print ('Connected to ', ip, ':', str(port))
            self.broadcast_to_all_clients(so)
            # 쓰레드 생성
            t = threading.Thread(target=self.receive_info, args=(so,))
            t.start()

    # 클라이언트 목록을 추가하는 함수
    def add_to_clients_list(self, client):
        if client not in self.clients_list:
            self.clients_list.append(client)

# 메인 함수
if __name__ == "__main__":
    threads = []
    thread_safe = True
    mutex = Lock()
    Server()