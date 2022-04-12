import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Host = socket.gethostname()
Port = 1235
s.bind((Host, Port))
s.listen(5)
client_socket, address = s.accept()
print(f"Connection to {address} established \n")
name = input("Enter the name of the img: \n")
ext = input("Enter the extension of your received file - jpg, png or bmp\n")
nwImg = name + "." + ext
file = open(nwImg, "wb")
image_data = client_socket.recv(2048)

while image_data:
      file.write(image_data)
      image_data = client_socket.recv(2048)
      
file.close()
client_socket.close()