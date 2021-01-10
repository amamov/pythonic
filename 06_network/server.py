import socket

# 서버 소켓 준비
server = socket.socket()
server.bind(("110.10.141.217", 9999))
server.listen(1)
print("-- Server is ready --")

# 클라이언트 접속 수락
client, addr = server.accept()
print("-- Client in connected --")

# 메세지 수신
message = client.recv(1024)
print("-- Message received --")

# 메세지 송신
client.sendall(b"Hello i'm server. your message is" + message)

# 헤제
client.close()
server.close()