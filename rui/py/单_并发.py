# 单进程单线程非阻塞实现并发服务器
import socket
import time


tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_server.bind(("", 7890))
tcp_server.listen(128)
# 设置套接字为非阻塞
tcp_server.setblocking(False)
cliet_socket_list = list()

while True:
    # time.sleep(2)
    try:
        new_socket, new_addr = tcp_server.accept()
    except Exception as e:
        print("---没有新客户端到来---")
    else:
        print("---只要没有发送异常就意味着新客户端的到来---")
        new_socket.setblocking(False)
        cliet_socket_list.append(new_socket)

    for cliet_socket in cliet_socket_list:
        try:
            recv_data = cliet_socket.recv(1024)
        except Exception as e:
            print("---客户端没有发送数据过来---")
        else:
            if recv_data:
                # 对方发送数据过来
                print("---客户端发送数据过来了---")
            else:
                cliet_socket_list.remove(cliet_socket)
                cliet_socket.close()
                print("---客户端已经关闭---")
