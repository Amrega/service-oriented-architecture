import MySQLdb

connection = MySQLdb.connect(
    host="localhost",
    user="root",
    passwd="",
    db="ais_db"
)
data_record = list()
table = "account"
row = "(`username`, `password`)"
data_record.insert(0, "coba")
data_record.insert(1, "cobas")

print(f"INSERT INTO `{table}` {row} VALUES (%s, %s);")
cursor = connection.cursor()
try:
    cursor.execute(f"INSERT INTO `{table}` {row} VALUES (%s, %s);", data_record)
    connection.commit()
except MySQLdb.Error as Error:
    print(Error)

else:

    cursor.execute("Select * from account;")

    db = cursor.fetchall()

    if db:
        for data in db:
            print(data)
    else:
        print('Not connected.')
