import socket


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 4600))
server.listen()

print('server is runed')


client, address = server.accept()
print(f'Client:{client}, adress: {address}')


file = open('image_server.jpg', mode='wb')
data = client.recv(2048)

while data:
    
    file.write(data)
    data = client.recv(2048)
    
    
file.close()
a = input()




