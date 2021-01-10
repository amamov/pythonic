import socket

# 서버 IP & port
ip = "110.10.141.217"
port = 9999

# 클라이언트 소켓 준비
client = socket.socket()

# 서버 접속
client.connect((ip, port))
print("-- Server is connected! --")

# 메세지 송신
client.send(b"Hello i'm client!")
print("-- Message send --")

# 메세지 수신
message = client.recv(1024)
print("-- Message received --")
print(message)

client.close()