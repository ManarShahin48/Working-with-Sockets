import socket


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Host = socket.gethostname()
Port = 12345
server.bind((Host, Port))
DNSTable = {
      "www.google.com" :"142.251.35.164" ,
      "www.facebook.com" :"157.240.214.35" ,
      "www.e-learn.suezuni.edu.eg" :"195.246.40.171"
}
server.listen(5)
Comunication_socket ,address = server.accept()
print(f"Connection to {address} established" )
while True :
      message = Comunication_socket.recv( 1024).decode( 'utf-8' )
      ip = DNSTable.get(message ,"Not Found" )
      Comunication_socket.send(ip.encode( 'utf-8' ))