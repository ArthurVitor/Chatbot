import mysql.connector
from random import randint

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="chatbot"
)
mycursor = mydb.cursor()


def cancel_appointment(number):
    mycursor.execute(f'''
    Delete From Clients
    Where Number = {number}
    ''')


def confirm_appointment(number, situation='To Confirm'):
    mycursor.execute(f'''
    Update Clients Set Situation='{situation}' Where Number={number};
    ''')


def add_client(name, number, hour, situation='To confirm'):
    mycursor.execute(f'''
    INSERT INTO clients (`Name`, `Number`, `Hour`, `Situation`)
    values ('{name}', '{number}', '{hour}', '{situation}')
    ''')


def gera_numero():
    num = randint(11111111111, 99999999999)
    return num


def gera_hora():
    hora = []
    d1 = randint(00, 23)  # Will generate the first two digits 00-23
    if d1 <= 9:
        d1 = str(d1)
        d1 = d1.zfill(2)
        hora.append(d1)
    else:
        hora.append(str(d1))

    d2 = randint(00, 59)  # Generate the 3th n 4th digits
    if d2 <= 9:
        d2 = str(d2)
        d2 = d2.zfill(2)
        hora.append(d2)
    else:
        hora.append(str(d2))

    d3 = randint(00, 59)
    if d3 <= 9:
        d3 = str(d3)
        d3 = d3.zfill(2)
        hora.append(d3)
    else:
        hora.append(str(d3))

    hora = ''.join(hora)
    return hora
