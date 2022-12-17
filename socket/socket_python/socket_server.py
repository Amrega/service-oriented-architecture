import socket
import MySQLdb
import json
import datetime

connection = MySQLdb.connect(
    host="localhost",
    user="root",
    passwd="",
    db="ais_db"
)

login = 0
cursor = connection.cursor()

def send(conn, data):
    conn.send(data.encode())

def myconverter(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()

def insert_data(data_record, table, row):
    try:
        cursor.execute(f"INSERT INTO `{table}` {row} VALUES (%s, %s);", data_record)
        connection.commit()
    except MySQLdb.Error as Error:
        print(Error)
        return 0
    else:
        return 1

def login(data_record):
    try:
        cursor.execute(f"Select * from `account` where `username`=%s and `password`=%s", data_record)
        db = cursor.fetchall()

        if db:
            login = 1
            return 1
        else:
            return 0
    except MySQLdb.Error as Error:
        print(Error)
        return 0

def get_data():
    try:
        cursor.execute(f"Select * from `account`")
        db = cursor.fetchall()

        if db:
            return json.dumps(db, default = myconverter)
        else:
            return 0
    except MySQLdb.Error as Error:
        print(Error)
        return 0

def menu():
    return """
        Selamat datang di program socket Traveloka, anda dapat memilih beberapa fitur :
        1. Register akun
        2. login
        3. lihat akun
        0. keluar
        """


def server_program():
    host = socket.gethostname()
    port = 5000  
    server_socket = socket.socket() 
    
    server_socket.bind((host, 5000))  

    server_socket.listen(2)
    conn, address = server_socket.accept()  
    print("Connection from: " + str(address))

    data = menu()
    conn.send(data.encode())
    while True:
        data_rec = int(conn.recv(1024).decode())
        print("client choose " + str(data_rec))

        if data_rec == 1:
            send(conn, "masukkan namamu")
            username = conn.recv(1024).decode()

            send(conn, "masukkan password")
            password = conn.recv(1024).decode()

            data_akun = list()
            data_akun.insert(0, username)
            data_akun.insert(1, password)
            
            if insert_data(data_akun, "account", "(`username`, `password`)"):
                send(conn, "berhasil register akun")
            else:
                send(conn, "gagal register akun")
        elif data_rec == 2:
            send(conn, "masukkan namamu")
            username = conn.recv(1024).decode()

            send(conn, "masukkan password")
            password = conn.recv(1024).decode()

            data_akun = list()
            data_akun.insert(0, username)
            data_akun.insert(1, password)
            
            if login(data_akun):
                send(conn, "berhasil login")
            else:
                send(conn, "gagal login")
        elif data_rec == 3:
            data_send = get_data()
            if data_send:
                send(conn, data_send)
            else:
                send(conn, "gagal mengambil data")
        elif data_rec == 0:
            break
        else:
            send(conn, "coming soon")

if __name__ == '__main__':
    server_program()