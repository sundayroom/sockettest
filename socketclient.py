import socket
import hashlib
import json
client=socket.socket()
try:
    client.connect(('127.0.0.1',5000))
except Exception :
    print("服务器未启动")
dic={}
def login(name,password):
    for k,v  in dic.items():
        if k!=name and v!=password:
            dic[name] = password
            print("登录成功")
        else:
            print("请输入正确的姓名和密码")
flag=True

while flag:
    msg=input(">>:请输入指令").split(" ")
    if len(msg)==0:continue
    if msg[0]=='/login':
        login(msg[1],msg[2])
    try:
        if msg[0]=='/quit':
            flag=False
    except Exception:
        client.close()
    print(len(msg))
    print(msg)
    data=msg[3]
    client.send(data.encode())
client.close()



    