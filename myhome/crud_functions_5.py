import sqlite3

connection = sqlite3.connect('products.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Products(
id INTEGER PRIMARY KEY,
title TEXT NOT NULL,
description TEXT,
price INTEGER NOT NULL
)
''')

cursor.execute("CREATE INDEX IF NOT EXISTS idx_description ON Products (description)")

# connection = sqlite3.connect('not_telegram_5.db')
# cursor = connection.cursor()
#
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users_5(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')
cursor.execute("CREATE INDEX IF NOT EXISTS idx_email ON Users_5 (email)")


# for i in range(1, 5):
#     cursor.execute("INSERT INTO Products(title, description, price) VALUES(?, ?, ?)",
#                    (f'Продукт{i}', f'Описание{i}', i * 100,))


# cursor.execute("DELETE FROM Products WHERE title = ?", ("Продукт4",))

def add_users(username, email, age):
    cursor.execute("INSERT INTO Users_5(username, email, age, balance) VALUES(?, ?, ?, ?)",
                   ('username', 'email', 'age', 1000,))


def is_included(us_name):
    check_users = cursor.execute('SELECT * FROM Users_5 WHERE username=?', (us_name,))
    us = cursor.fetchone()
    if us is not None:
        us = True
    else:
        us = False
    return us


def get_all_products():
    cursor.execute('SELECT * FROM Products')
    pr = cursor.fetchall()
    for prod in pr:
        print(f'Название {prod[1]}| Описание {prod[2]}| Цена {prod[3]}')
    print(pr)
    return pr


# get_all_products()

connection.commit()
# connection.close()
