import re
import select
import socket


def server_client(new_socket, request):
    """为这个客户端返回数据"""
    # 1.接受浏览器发送过来的请求，即http请求
    # GET / HTTP/1.1
    # request = new_socket.recv(1024).decode('utf-8')
    request_lines = request.splitlines()
    # print(request)
    print('>' * 20)
    print(request_lines)
    # GET /index.html HTTP/1.1
    ret = re.match(r"[^/]+(/[^ ]*)", request_lines[0])
    fine_name = ""
    if ret:
        fine_name = ret.group(1)
        if fine_name == '/':
            fine_name = '/index.html'
    # 2.返回http格式的数据给浏览器
    try:
        f = open("." + fine_name, 'rb')
    except:
        response = "HTTP/1.1 404 NOT FOUND\r\n"
        response += '\r\n'
        response += "------file not found-------"
        new_socket.send(response.encode('utf-8'))
    else:
        html_content = f.read()
        f.close()
        response_body = html_content
        response_header = "HTTP/1.1 200 OK\r\n"
        response_header += "Content-Length:%d\r\n" % len(response_body)
        response_header += "\r\n"
        response = response_header.encode('utf-8') + response_body
        new_socket.send(response)


def main():
    """用来完成整体的控制"""
    # 1.创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # 2.绑定
    tcp_server_socket.bind(("", 7890))
    # 3.变为监听模式
    tcp_server_socket.listen(128)
    tcp_server_socket.setblocking(False)

    #  创建一个epoll对象
    # epl = select.epoll()
    # epl.register(tcp_server_socket.fileno(), select.EPOLLIN)
    client_socket_list = list()
    while True:
        # 4.等待新客户端的连接
        try:
            new_socket, client_addr = tcp_server_socket.accept()
        except Exception as e:
            pass
        else:
            new_socket.setblocking(False)
            client_socket_list.append(new_socket)
        for client_socket in client_socket_list:
            try:
                recv_data = client_socket.recv(1024).decode('utf-8')
            except Exception as e:
                pass
            else:
                if recv_data:
                    server_client(client_socket, recv_data)
                else:
                    client_socket.close()
                    client_socket_list.remove(client_socket)
    # 关闭监听套接字
    tcp_server_socket.close()


if __name__ == '__main__':
    main()