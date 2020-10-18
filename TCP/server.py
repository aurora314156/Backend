import socket, threading, time

MAX_CONNECTION_NUMBER = 5
MAX_MESSAGE_LIMIT = 1024 # bytes
PORT = 9999
IP = '127.0.0.1'

def tcp_link(sock, addr):
    print(f'Accpet new connection from {sock} {addr}...')
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(MAX_MESSAGE_LIMIT) # max recv bytes 1k
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        data = data.decode('utf-8')
        msg = (f'Hello, {data}').encode('utf-8')
        sock.send(msg)
    sock.close() # close connection
    print('Connection from {sock} {addr} close.')

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # create socket
    s.bind((IP, PORT)) # bind port
    s.listen(MAX_CONNECTION_NUMBER) # listening port
    print('Waiting for connection')
    while True:
        sock, addr = s.accept() # accept new connection
        t = threading.Thread(target=tcp_link, args=(sock, addr)) # create new thread for TCP connection
        t.start()

if __name__ == "__main__":
    main()