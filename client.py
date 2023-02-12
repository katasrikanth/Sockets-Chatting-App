import socket
import threading

HOST = socket.gethostbyname(socket.gethostname())
PORT= 3421


def listen_for_messages_from_server(client):
    while(True):
        message = client.recv(2024).decode('utf-8')
        if message != "":
            username = message.split("~")[0]
            content = message.split("~")[1]
            print(f"{username} {content}")
        else:
            print("Message received from client is empty")


def send_message_to_server(client):
    while(True):
        message = input("Message: ")
        if message!="":
            client.sendall(message.encode())
        else:
            print("Empty message")
            exit(0)         


def communicate_to_server(client):
       username = input("Enter username: ")   
       if username != '':
           client.sendall(username.encode())
       else:
           print("Username cannot be empty")
           exit(0)
       threading.Thread(target=listen_for_messages_from_server, args=(client, )).start()
       send_message_to_server(client)

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

try:
    client.connect((HOST,PORT))
    print(f"Successfully connected to server")
except:
     print(f"unable to connect to server {HOST} {PORT} ")

communicate_to_server(client)


