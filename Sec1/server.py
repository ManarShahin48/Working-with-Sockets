import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Host=socket.gethostname()
Port=1234
s.bind((Host,Port))
s.listen( 5)
while True:
      Comunication_socket,address=s.accept()
      print(f"Connection to {address} established" )
      message=Comunication_socket.recv( 1024).decode( 'utf-8')
      print(f"Message from client : {message} ")
      Comunication_socket.send(( "Hi client , I'm server sending u a message" ).encode('utf-8'))
      Comunication_socket.close()
      print(f"Communication Ended" )