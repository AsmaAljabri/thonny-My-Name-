
"""
in this problem, is to make a proggram to calculate the number of files times the capacity of each if it is the answer will be equal to the 
computer storage 
by asking the user to enter the inputs X (computer storage), n (number of file), y (capacity of the file) 
using if else statement
"""
x = int( input("please enter the computer storage = "))
n = int( input("please enter the number of files you want  = "))
y = int( input("please enter the capacity of the file  = "))

if ( x >= n * y):
    print("yes")

else:
    print("no")

