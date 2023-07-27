

n = int( input("please enter the number of the subjects = "))
x = int( input("please enter the number of days for each subject  = "))
y = int( input("please enter the number of days until the tests start   = "))

if ( y >= n * x):
    print("yes")

else:
    print("no")