import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')
cursor.execute("CREATE INDEX IF NOT EXISTS idx_email ON Users (email)")
# for i in range(1, 11):
#     cursor.execute("INSERT INTO Users(username, email, age, balance) VALUES(?, ?, ?, ?)",
#                     (f'user{i}', f'example{i}@gmail.com', f'{i * 10}', '1000'))
# cursor.execute("DELETE FROM users WHERE username = ?", ("user0",))
#for j in range(1, 11, 2):
#    cursor.execute("UPDATE Users SET balance = ? WHERE username = ?", (500, f"user{j}"))
#for x in range(1, 11, 3):
#    cursor.execute("DELETE FROM users WHERE username = ?", (f"user{x}",))

cursor.execute("SELECT username, email, age, balance FROM Users WHERE age != ?", (60,))
users = cursor.fetchall()
for user_ in users:
    print(f'Имя {user_[0]}| Почта {user_[1]}| Возраст {user_[2]}| Баланс {user_[3]}')


connection.commit()
connection.close()
