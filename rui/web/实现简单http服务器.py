import re
import socket
import multiprocessing


class WSGIServer():
    def __init__(self):
        # 1.创建套接字
        self.tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # 2.绑定
        self.tcp_server_socket.bind(("", 7890))
        # 3.变为监听模式
        self.tcp_server_socket.listen(128)

    def server_client(self, new_socket):
        """为这个客户端返回数据"""

        # 1.接受浏览器发送过来的请求，即http请求
        # GET / HTTP/1.1
        request = new_socket.recv(1024).decode('utf-8')
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
                fine_name = './py/index.html'
            # print('*' * 20, fine_name)

        # 2.返回http格式的数据给浏览器
        try:
            f = open("./" + fine_name, 'rb')
        except:
            response = "HTTP/1.1 404 NOT FOUND\r\n"
            response += '\r\n'
            response += "------file not found-------"
            new_socket.send(response.encode('utf-8'))
        else:
            html_content = f.read()
            f.close()
            # 2.1准备发给浏览器的数据--header
            response = "HTTP/1.1 200 OK\r\n"
            response += "\r\n"
            # 2.2准备发送给浏览器的数据--body
            # response += "<h1>hahaha</h1>"
            # 将response header发送给浏览器
            new_socket.send(response.encode('utf-8'))
            # 将response body发送给浏览器
            new_socket.send(html_content)

        # 关闭套接字
        new_socket.close()

    def run_forever(self):
        """用来完成整体的控制"""
        while True:
            # 4.等待新客户端的连接
            new_socket, client_addr = self.tcp_server_socket.accept()
            # 5.为这个客户端服务
            # 多进程
            p = multiprocessing.Process(target=self.server_client, args=(new_socket,))
            p.start()
            # 多进程中，子进程复制父进程的全部资源，所有要多关闭套接字一次
            new_socket.close()
            # 多线程，共享资源
            # p = threading.Thread(target=server_client, args=(new_socket,))
            # p.start()
            # gevent.spawn(server_client, new_socket)

        self.tcp_server_socket.close()


def main():
    wsgi_server = WSGIServer()
    wsgi_server.run_forever()


if __name__ == '__main__':
    main()