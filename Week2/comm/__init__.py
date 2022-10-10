import threading

def listenAndSend(client_socket):
    read_thread = threading.Thread(listen, args=(client_socket,))
    read_thread.start()

    while True:
        buffer = input()
        buffer += '\n'
        client_socket.send(buffer.encode())

def listen(socket):
    while True:
        recv_len = 1
        response = ''
        while recv_len:
            data = client_socket.recv(4096)
            recv_len = len(data)
            response += data.decode()
            if recv_len < 4096:
                break
        if response:
            print(response, end='')
