"""
make a program to encripte the user enter into readable value using ascii and od methods 
"""

messege = input("please enter the message")  

for i in messege:
    ASCII = int( ord(i)-3)
    print(chr(ASCII), end = "")
