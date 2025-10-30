import string
import random

length=int(input("Enter password length:  "))
Character_list=""
print ('''Choice any of your password type sir as you like:
            1.Letters
            2.Digits
            3.Special letters
            4.Exit
       ''')
while (True):
    choice=int(input('Pick up number (From:1-4):  '))
    if choice==1:
        Character_list+=string.ascii_letters
    elif choice==2:
        Character_list+=string.digits
    elif choice==3:
        Character_list+=string.punctuation
    elif choice==4:
        break

Password=[]

for i in range (length):
    randomchar=random.choice(Character_list)
    Password.append(randomchar)
print()
print ("The password is  "+"".join(Password))