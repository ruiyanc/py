import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 发出连接请求
s.connect(("127.0.0.1", 6000))
print(s.recv(1024).decode("utf-8"))
data = "client"
while True:
    if data:
        print(s.recv(1024).decode("utf-8"))
    data = input("Please input your name: ")
    if not data:
        continue
    # 向套接字对象发送数据
    s.send(data.encode("utf-8"))
    # 接收数据并解码
    print(s.recv(1024).decode("utf-8"))
    if data == "exit":
        break
s.close()
