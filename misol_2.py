import csv

users = []
with open('users_info.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(['ID', 'NAME', 'LASTNAME', 'AGE', 'ADDRES', 'EMAIL', 'PHONE'])
def add_user(id, name, lastname, age, addres, email, phone):
    user = {
        'id': id,
        'name': name,
        'lastname': lastname,
        'age': age,
        'addres': addres,
        'email': email,
        'phone': phone
    }
    return user

def add_user_csv(user_dict):
    with open('users_info.csv', 'a') as file:
        writer = csv.writer(file, lineterminator='\n')
        for use in user_dict:
            writer.writerow(use.values())

id = 0
while True:
    id += 1
    name = input("Ism: ")
    if name == 'stop':
        add_user_csv(users)
        break
    lastname = input("Familiya: ")
    age = int(input("Yosh: "))
    addres = input("Addres: ")
    email = input('Email: ')
    phone = input('Tel: ')
    us = add_user(id, name, lastname, age, addres, email, phone)
    users.append(us)
    print(users)
