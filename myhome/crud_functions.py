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


# for i in range(1, 5):
#     cursor.execute("INSERT INTO Products(title, description, price) VALUES(?, ?, ?)",
#                    (f'Продукт{i}', f'Описание{i}', i * 100,))


# cursor.execute("DELETE FROM Products WHERE title = ?", ("Продукт4",))
def get_all_products():
    cursor.execute('SELECT * FROM Products')
    pr = cursor.fetchall()
    for prod in pr:
        print(f'Название {prod[1]}| Описание {prod[2]}| Цена {prod[3]}')
    print(pr)
    return pr


get_all_products()

connection.commit()
# connection.close()
