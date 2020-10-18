import socket

PORT = 9999
IP = '127.0.0.1'
MAX_MESSAGE_LIMIT = 1024 # byte

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # create socket
    s.connect((IP, PORT)) # create connection
    print(s.recv(MAX_MESSAGE_LIMIT).decode('utf-8')) # recv message from server
    name = [b'Rick', b'Jack', b'Turtle']
    for data in name:
        s.send(data) # socket send data
        print(s.recv(MAX_MESSAGE_LIMIT).decode('utf-8')) # recv message from server
    s.send(b'exit')
    s.close()

if __name__ == "__main__":
    main()