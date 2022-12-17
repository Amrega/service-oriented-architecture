import socket


def client_program():
    host = socket.gethostname() 
    port = 5000  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, 5000))  # connect to the server

    message = ""
    while message.lower().strip() != "0":
        data = client_socket.recv(1024).decode()  
        print('Received from server: ' + data)  

        message = input(" -> ")
        client_socket.send(message.encode())  
          
    client_socket.close()  

if __name__ == '__main__':
    client_program()