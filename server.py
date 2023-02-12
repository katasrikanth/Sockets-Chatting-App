
from email.mime import message
import socket
import threading

HOST = socket.gethostbyname(socket.gethostname())
PORT= 3421
LIMIT = 5
active_clients = []

def listen_for_message(client, username):
      
      while(True):
          message = client.recv(2024).decode('utf-8')
          if message !='':
               final_msg = username + " ~ " + message
               send_messages_to_all(final_msg)
          else:    
             print(f"The message send from client {username} is empty")


def send_message_to_client(client, message):
       client.send(message.encode())

def send_messages_to_all(message):
     for user in active_clients:
             send_message_to_client(user[1], message)


def client_handler(client):
    
    while(True):
        username = client.recv(2024).decode('utf-8')
        if username != "":
             active_clients.append((username, client))
             break
        else:
            print("client username is empty")
    
    threading.Thread(target=listen_for_message, args=(client, username, )).start()

server  = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

try:
     server.bind((HOST, PORT))
     print(f"Server is runnnig Successfully on {HOST} {PORT}")
except:
    print("unable to bind to Host, Check Host!")


server.listen(LIMIT)

while(True):
    client, address= server.accept()
    print(f"Successfully connected to client {address[0]} {address[1]}")
 
    threading.Thread(target=client_handler, args=(client, )).start()