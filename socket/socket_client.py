import socket


def client_program():
    host = socket.gethostname()  # as both code is running on same pc
    #port = 5000  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, 5000))  # connect to the server

    messageN = input(" -> Username : ")  # take input
    messageH = input(" -> Nomor HP : ")
    messageE = input(" -> Email : ")
    
    while messageN.lower().strip() != 'bye':
        client_socket.send(messageN.encode())  # send message
        dataN = client_socket.recv(1024).decode()  # receive response

        print('Received from server: ' + dataN)  # show in terminal

        messageN = input(" -> ")  # again take input

    client_socket.close()  # close the connection



    while messageH.lower().strip() != 'bye':
        client_socket.send(messageH.encode())  # send message
        dataH = client_socket.recv(1024).decode()  # receive response

        print('Received from server: ' + dataH)  # show in terminal

        messageH = input(" -> ")  # again take input

    client_socket.close()  # close the connection

    
    while messageE.lower().strip() != 'bye':
        client_socket.send(messageE.encode())  # send message
        dataE = client_socket.recv(1024).decode()  # receive response

        print('Received from server: ' + dataE)  # show in terminal

        messageE = input(" -> ")  # again take input

    client_socket.close()  # close the connection




if __name__ == '__main__':
    client_program()