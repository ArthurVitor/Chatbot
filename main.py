from idlelib.debugobj import myrepr
import mysql.connector, random as rd


# mydb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     passwd="",
#     database="chatbot"
# )

nums = [0,0]
f = open('horas.txt', 'w')
for c in range(0, 48):
    f.write(f'{nums[0]}:{nums[1]} \n')
    nums[1] += 30
    if nums[1] == 60:
        nums[0] += 1
        nums[1] = 0
f.close()