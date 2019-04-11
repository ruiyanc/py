import socket
import threading


def tcp_link(conn, addr):
    print("Accept new connection from %s:%s" % addr)
    conn.send(b"Welcome!\n")
    while True:
        conn.send(b"What's your name?")
        # 接收客户端发来的bytes对象
        data = conn.recv(1024)
        if data == b"exit":
            conn.send(b"Good bye!\n")
            break
        conn.send(b"Hello %s!\n" % data)
    conn.close()
    print("Connection from %s:%s is closed" % addr)


# SOCK_STREAM为tcp协议的网络通信
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 绑定ip地址和端口
s.bind(("127.0.0.1", 6000))
# 开启监听功能，等待客户端的连接请求
s.listen(5)
print("Waiting for connection...")
while True:
    # 获得客户端的host和port二元组
    conn, addr = s.accept()
    # 多线程，target后接函数名
    t = threading.Thread(target=tcp_link, args=(conn, addr))
    t.start()
