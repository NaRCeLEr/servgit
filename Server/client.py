import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 4600))

print('server is runed')
print ("Hello")
print("It is aboyt branch")

file = open('nikebag2.jpg', mode='rb')
data = file.read(2048)

while data:
    client.send(data)
    data = file.read(2048)

file.close()


a = input()



