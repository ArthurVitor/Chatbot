import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="chatbot"
)

mycursor = mydb.cursor()
mycursor.execute("SHOW TABLES")

for tb in mycursor: #Show all chatbot tables
    print(tb)