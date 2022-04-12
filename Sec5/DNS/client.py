import socket


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Host = socket.gethostname()
Port = 12345
client.connect((Host, Port))
c = "y"
while c == "y":
      domain = input("Enter the domian name : \n")
      client.send(domain.encode('utf-8'))
      message = client.recv(1024).decode('utf-8')
      print(message)
      c = input("Continue? (y / n)\n")
client.close()