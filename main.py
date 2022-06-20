import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="chatbot"
)

mycursor = mydb.cursor()
mycursor.execute("""
insert into clients
(nome, number, situation)
values
("Dummy1", "83987806418", "OFF")
""")

#Data base example
#Arthur	83987806698	OFF
#Dummy1	83987806418	OFF
