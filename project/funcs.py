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
    delete from toconfirm 
    where Number = {number}
    ''')

def ConfirmAppointment(number):
    #Criar algo que vai ler as informações da pessoa com o número e colocar na Table "Confirmed"
    pass