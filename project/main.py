import mysql.connector, funcs

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="chatbot"
)

_rehours = []
mycursor = mydb.cursor()

funcs.ConfirmAppointment('83987806698')