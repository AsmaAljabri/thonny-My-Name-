# make a program to calculator two inputs, where the user will enter  the numbers and the opreator

num1 = float(input("enter  number1: "))
num2 = float(input("enter  number2: "))
oper = input("enter operator: ")

"""compound if else statement
"""
if (oper =='+'):
    print(num1 + num2 )
elif (oper =='-'):
    print(num1 - num2 )
elif (oper =='/'):
    print(num1 / num2 )
elif (oper =='*'):
    print(num1 * num2 )
elif (oper =='**'):
    print(num1 ** num2 )
else:
    print("Invlid operator")
