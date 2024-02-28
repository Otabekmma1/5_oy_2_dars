import sqlite3 as sql
connection = sql.connect('users.db')
cursor = connection.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PIMARY KEY,
    name VARCHAR(20),
    lastname VARCHAR(20),
    age INTEGER,
    addres VARCHAR(50),
    email VARCHAR(50),
    phone VARCHAR(30)
)
''')
connection.commit()

users = []
def add_user(name, lastname, age, addres, email, phone):
    users.extend([name, lastname, age, addres, email, phone])
    return users

def add_sqlite(user_list: list):
    cursor.executemany('''
        INSERT INTO users(name, lastname, age, addres, email, phone) VALUES (?, ?, ?, ?, ?, ?)
        ''', user_list)
    connection.commit()
    connection.close()

while True:
    name = input("Ism: ")
    if name == 'stop':
        add_sqlite(users)
        print("Ma'lumotlar users.db ga qo'shildi")
        break

    lastname = input("Familiya: ")
    age = int(input("Yosh: "))
    addres = input("Addres: ")
    email = input('Email: ')
    phone = input('Tel: ')
    add_user(name, lastname, age, addres, email, phone)
    print(users)

connection.close()