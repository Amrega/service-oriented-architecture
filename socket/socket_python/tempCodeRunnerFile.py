    cursor.execute("Select * from account;")

    db = cursor.fetchall()

    if db:
        for data in db:
            print(data)
    else:
        print('Not connected.')
