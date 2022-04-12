import socket


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect(("www.facebook.com", 80))
server.sendall(b"GET/HTTP/1.1\nHost:www.facebook.com\n")
print(server.recv(4096).decode('utf-8'))