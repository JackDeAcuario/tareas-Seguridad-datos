import socket

target_host = "www.google.com"
target_port = 80
codigo = "GET / HTTP/1.1\r\nHost: google.com\r\n\r\n"

#create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connect to client
client.connect((target_host,target_port))

#send some data
client.send(codigo.encode())

#receive some data
response = client.recv(4096)

print(response)