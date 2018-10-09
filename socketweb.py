import socket
import hashlib


def handle_request(client):
    buf=client.recv(1024)
    client.send("HTTP/1.1 200 OK\r\n\r\n")
    client.send("Hello world")

def main():
    sock=socket.socket()
    sock.bind(('127.0.0.1',6000))
    sock.listen(5)

    while True:
        conn,address=sock.accept()
        handle_request(conn)
        conn.close()

if __name__=='__main__':
    main()

