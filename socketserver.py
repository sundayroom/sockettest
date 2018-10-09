import socket
import os
import hashlib
server=socket.socket()
server.bind(('127.0.0.1',5000))
server.listen(5)#开始监听
print("等待连接中")
while True:
    conn,address=server.accept()
    print(os.path)
    print("***连接成功***")
    while True:
        data=conn.recv(1024)
        print("接收到的内容为:",data)
        if not data:
            print("客户端断开连接")
            break


server.close()


