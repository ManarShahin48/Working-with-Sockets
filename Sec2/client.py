########################## TCP ##########################
# import socket
# socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Host=socket.gethostname()
# Port=1234
# socket_client.connect((Host,Port))
# socket_client.send(("Hi server , I'm the Client").encode('utf-8'))
# message=socket_client.recv(1024).decode('utf-8')
# print(f"Message from the server : {message}")

########################## UDP ##########################
import socket
socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Host=socket.gethostname()
Port=1234
socket_client.connect((Host,Port))
while True:
      msg_toSend=input("entr a msg")
      socket_client.send((msg_toSend).encode('utf-8'))
      message=socket_client.recv(1024).decode('utf-8')
      print(f"msg from the server : {message}")