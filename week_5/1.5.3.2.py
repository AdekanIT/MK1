import sqlite3

conn = sqlite3.connect('my_users.db')
sql = conn.cursor()
sql.execute('CREATE TABLE IF NOT EXISTS users'
            '(user_id INTEGER, username TEXT);')
# sql.execute('INSERT INTO users(user_id, username) VALUES(0, "Lord");')
# sql.execute('INSERT INTO users(user_id, username) VALUES(1, "Keny");')
# sql.execute('INSERT INTO users(user_id, username) VALUES(2, "Grid");')
# sql.execute('INSERT INTO users(user_id, username) VALUES(3, "Salamon");')
# sql.execute('INSERT INTO users(user_id, username) VALUES(4, "Mine");')

sql.execute('SELECT user_id FROM users;')
sql.execute('DELETE FROM users WHERE username = "Mine";')
sql.execute('UPDATE users SET username = "West" WHERE user_id = 1;')
id = int(input('Enter id: '))
print(sql.execute('SELECT user_id, username FROM users;').fetchall())
print(sql.execute(f'SELECT user_id, username FROM users WHERE user_id = {id};').fetchall())
# print(sql.execute('SELECT user_id, username FROM users WHERE user_id = 3;').fetchone())
# print(sql.execute('SELECT user_id, username FROM users WHERE user_id = 3;').fetchall())
# print(sql.execute('SELECT user_id, username FROM users;').fetchone())



conn.commit()