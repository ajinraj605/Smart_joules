import json
import socket


def client_program():
    host = socket.gethostname()  # as both code is running on same pc
    port = 5000  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server

    cmd_array = '[{"method": "mkdir /tmp/temp_file", "id": "242c41d4-2cc5-4cfb-b815-89e33862e125"}, ' \
                '{"method": "sudo rm -rf directory ", "id": "242c41d4-2cc5-4cfb-b815-89e33862e126"}, ' \
                '{"method": "ls", "id": "242c41d4-2cc5-4cfb-b815-89e33862e127"}, ' \
                '{"method": "mkdir /tmp/temp_file", "id": "242c41d4-2cc5-4cfb-b815-89e33862e128"}, ' \
                '{"method": "mkdir /tmp/temp_file", "id": "242c41d4-2cc5-4cfb-b815-89e33862e129"},' \
                ' {"method": "mkdir /tmp/temp_file", "id": "242c41d4-2cc5-4cfb-b815-89e33862e122"}]'
    message = str(json.loads(cmd_array))

    while message != ' ':
        client_socket.send(message.encode())  # send message
        data = client_socket.recv(1024).decode()  # receive response
        print('Received from server: ' + data)  # show in terminal
        message = input(" -> ")  # again take input

    client_socket.close()  # close the connection


if __name__ == '__main__':
    client_program()