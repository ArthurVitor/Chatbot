import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="chatbot"
)
mycursor = mydb.cursor()


def CancelAppointment(number):
    mycursor.execute(f'''
    Delete From Clients 
    Where Number = {number}
    ''')


def ConfirmAppointment(number, situation='To Confirm'):
    mycursor.execute(f'''
    Update Clients Set Situation='{situation}' Where Number={number};
    ''')
