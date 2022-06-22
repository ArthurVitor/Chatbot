from idlelib.debugobj import myrepr

import mysql.connector, random as rd

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="chatbot"
)

def read_file(file):
    x = open(file,'r', encoding = 'utf-8')
    y = x.read()
    content = y.splitlines()
    return content

chat = read_file('Chats/Conversa do WhatsApp com Ravel.txt')
print(len(chat))