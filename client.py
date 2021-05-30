from tkinter import Tk, Button, Frame, Scrollbar, Label, END, Entry, Text, VERTICAL
import tkinter as tk
import socket
import threading
from tkinter import messagebox


class ChatClient:
    americano=30
    latte=30
    smoothie = 30
    coldbrew = 30
    espresso = 30
    waffle= 30
    latte = 30
    prafe = 30
    client_socket = None
    last_received_message = None

    

    def __init__(self, root):
        
        self.root = root
        self.label = tk.Label(self.root, text = '남은 수량').grid(row = 10, column = 100)
        self.text=tk.StringVar()
        self.text.set("Americano 남은수량")
        self.label9=tk.Label(self.root,textvariable=self.text)
        self.button1=tk.Button(self.root,text='새로고침',command=self.changeText1)
        self.label9.grid(row = 40, column = 100, padx = 10, pady = 10)
        self.button1.grid(row = 40, column = 70, padx = 10, pady = 10)

        self.text1=tk.StringVar()
        self.text1.set("latte 남은수량")
        self.label10=tk.Label(self.root,textvariable=self.text1)
        self.button2=tk.Button(self.root,text="새로고침",command=self.changeText2)
        self.label10.grid(row = 70, column = 100, padx = 10, pady = 10)
        self.button2.grid(row = 70, column = 70, padx = 10, pady = 10)

        self.text2=tk.StringVar()
        self.text2.set("waffle 남은수량")
        self.label11=tk.Label(self.root,textvariable=self.text2)
        self.button3=tk.Button(self.root,text="새로고침",command=self.changeText3)
        self.label11.grid(row = 100, column = 100, padx = 10, pady = 10)
        self.button3.grid(row = 100, column = 70, padx = 10, pady = 10)
        
        self.text3=tk.StringVar()
        self.text3.set("smoothie 남은수량")
        self.label12=tk.Label(self.root,textvariable=self.text3)
        self.button4=tk.Button(self.root,text="새로고침",command=self.changeText4)
        self.label12.grid(row = 130, column = 100, padx = 10, pady = 10)
        self.button4.grid(row = 130, column = 70, padx = 10, pady = 10)

        self.text4=tk.StringVar()
        self.text4.set("cold brew 남은수량")
        self.label13=tk.Label(self.root,textvariable=self.text4)
        self.button5=tk.Button(self.root,text="새로고침",command=self.changeText5)
        self.label13.grid(row = 160, column = 100, padx = 10, pady = 10)
        self.button5.grid(row = 160, column = 70, padx = 10, pady = 10)

        self.text5=tk.StringVar()
        self.text5.set("espresso 남은수량")
        self.label14=tk.Label(self.root,textvariable=self.text5)
        self.button6=tk.Button(self.root,text="새로고침",command=self.changeText6)
        self.label14.grid(row = 190, column = 100, padx = 10, pady = 10)
        self.button6.grid(row = 190, column = 70, padx = 10, pady = 10)

        self.text6=tk.StringVar()
        self.text6.set("prafe 남은수량")
        self.label15=tk.Label(self.root,textvariable=self.text6)
        self.button7=tk.Button(self.root,text="새로고침",command=self.changeText7)
        self.label15.grid(row = 220, column = 100, padx = 10, pady = 10)
        self.button7.grid(row = 220, column = 70, padx = 10, pady = 10)


        self.initialize_socket()
        self.initialize_gui()
        self.listen_for_incoming_messages_in_a_thread()

    def changeText1(self):
        self.text.set(self.americano)
    def changeText2(self):
        self.text1.set(self.latte)
    def changeText3(self):
        self.text2.set(self.waffle)
    def changeText4(self):
        self.text3.set(self.smoothie)
    def changeText5(self):
        self.text4.set(self.coldbrew)
    def changeText6(self):
        self.text5.set(self.espresso)
    def changeText7(self):
        self.text6.set(self.prafe)
        
    def initialize_socket(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        remote_ip = '220.66.218.156'
        remote_port = 50005
        self.client_socket.connect((remote_ip, remote_port))

    def initialize_gui(self):
        self.display_name_section()
        self.americano1()
        self.latte1()
        self.waffle1()
        self.smoothie1()
        self.coldbrew1()
        self.espresso1()
        self.prafe1()
        self.display_chat_transcript()

    def listen_for_incoming_messages_in_a_thread(self):
        t = threading.Thread(
            target=self.receive_message_from_server, args=(self.client_socket,))
        t.start()

    def americano1(self):

        def click_americano():
            if self.americano <= 0:
                button1['state'] = tk.DISABLED
            if self.americano >= 1:
                self.enter_text_widget = "americano 1"
                self.send_chat()

        label1 = Label(self.root, text = 'americano')
    
        label1.grid(row = 40, column = 10)
        button1 = Button(self.root, text = 'buy', width = 5, command = click_americano)
        button1.grid(row = 40, column = 30)
       
            
    def latte1(self):
        def click_americano():
            if self.latte <= 0:
                button1['state'] = tk.DISABLED
            if self.latte >= 1:
                self.enter_text_widget = "latte 1"
                self.send_chat()

        label1 = Label(self.root, text = 'Latte ')
        label1.grid(row = 70, column = 10)
        button1 = Button(self.root, text = 'buy', width = 5, command = self.click_latte)
        button1.grid(row = 70, column = 30)

    def waffle1(self):
        def click_waffle():
            if self.waffle <= 0:
                button1['state'] = tk.DISABLED
            if self.waffle >= 1:
                self.enter_text_widget = "waffle 1"
                self.send_chat()

        label1 = Label(self.root, text = 'waffle ')
        label1.grid(row = 100, column = 10)
        button1 = Button(self.root, text = 'buy', width = 5, command = self.click_waffle)
        button1.grid(row = 100, column = 30)

    def smoothie1(self):
        def click_smoothie():
            if self.smoothie <= 0:
                button1['state'] = tk.DISABLED
            if self.smoothie >= 1:
                self.enter_text_widget = "smoothie 1"
                self.send_chat()

        label1 = Label(self.root, text = 'smoothie ')
        label1.grid(row = 130, column = 10)
        button1 = Button(self.root, text = 'buy', width = 5, command = self.click_waffle)
        button1.grid(row = 130, column = 30)

    def coldbrew1(self):   
        def click_coldbrew():
            if self.coldbrew <= 0:
                button1['state'] = tk.DISABLED
            if self.coldbrew >= 1:
                self.enter_text_widget = "coldbrew 1"
                self.send_chat()

        label1 = Label(self.root, text = 'cold brew ')
        label1.grid(row = 160, column = 10)
        button1 = Button(self.root, text = 'buy', width = 5, command = self.click_waffle)
        button1.grid(row = 160, column = 30)

    def espresso1(self):
        def click_espresso():
            if self.espresso <= 0:
                button1['state'] = tk.DISABLED
            if self.espresso >= 1:
                self.enter_text_widget = "espresso 1"
                self.send_chat()

        label1 = Label(self.root, text = 'espresso ')
        label1.grid(row = 190, column = 10)
        button1 = Button(self.root, text = 'buy', width = 5, command = self.click_waffle)
        button1.grid(row = 190, column = 30)
    
    def prafe1(self):
        def click_prefe():
            if self.prafe <= 0:
                button1['state'] = tk.DISABLED
            if self.prafe >= 1:
                self.enter_text_widget = "prafe 1"
                self.send_chat()

        label1 = Label(self.root, text = 'prafe ')
        label1.grid(row = 220, column = 10)
        button1 = Button(self.root, text = 'buy', width = 5, command = self.click_waffle)
        button1.grid(row = 220, column = 30)


    def receive_message_from_server(self, so):
        while True:
            buf = so.recv(256)
            if not buf:
                break
            self.chat_transcript_area.insert('end', buf.decode('utf-8') + '\n')
            text=buf.decode('utf-8')
            if text[0]==' ':
                self.americano,self.latte,self.waffle, self.smoothie, self.coldbrew, self.espresso, self.prafe =map(int,text[1:].split())

            self.chat_transcript_area.yview(END)
        so.close()

    def display_name_section(self):
        frame = Frame()
        Label(frame, text='Enter your name:').grid(row = 10, column = 10)
        self.name_widget = Entry(frame, width=30)
        self.name_widget.grid(row = 10, column = 20)
        frame.grid(row = 10, column = 10)

    def display_chat_transcript(self):
        frame = Frame()
        Label(frame, text='카페 주문').grid(row = 0, column = 0, padx = 10, pady = 10)

        self.chat_transcript_area = Text(frame, width=60, height=20)
        scrollbar = Scrollbar(
            frame, command=self.chat_transcript_area.yview, orient=VERTICAL)
        self.chat_transcript_area.config(yscrollcommand=scrollbar.set)
        self.chat_transcript_area.bind('<KeyPress>', lambda e: 'break')
        self.chat_transcript_area.grid(row = 230, column = 10)
        frame.grid(row = 230, column = 10, padx = 10, pady = 10)

    def display_chat_entrybox(self):
        frame = Frame()
        Label(frame, text='Enter chat messages:')
        self.enter_text_widget = Text(frame, width=60, height=8)
        scrollbar = Scrollbar(
            self.root, command=self.enter_text_widget.yview, orient=VERTICAL)
        self.enter_text_widget.config(yscrollcommand=scrollbar.set)
        self.enter_text_widget.bind('<Return>', self.on_enter_key_pressed)

    def on_enter_key_pressed(self, event):
        if len(self.name_widget.get()) == 0:
            messagebox.showerror(
                "Enter your name", "Enter your name to send a message")
            return
        self.send_chat()
        self.clear_text()

    def clear_text(self):
        self.enter_text_widget.delete(1.0, 'end')
    def send_chat1(self):
        senders_name = self.name_widget.get()
        data = self.enter_text_widget.strip()
        message = (senders_name + data).encode('utf-8')
        self.chat_transcript_area.insert('end', message.decode('utf-8') + '\n')
        self.chat_transcript_area.yview(END)
        self.client_socket.send(message)
        return 'break'
    def send_chat(self):
        senders_name = self.name_widget.get().strip() + ":"
        data = self.enter_text_widget.strip()
        message = (senders_name + data).encode('utf-8')
        self.chat_transcript_area.insert('end', message.decode('utf-8') + '\n')
        self.chat_transcript_area.yview(END)
        self.client_socket.send(message)
        return 'break'

if __name__ == '__main__':
    root = Tk()
    root.title("cafe")
    ChatClient(root)
    root.mainloop()