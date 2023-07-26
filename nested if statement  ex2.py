"""

nested if statement  ex2
"""
Gender = input("enter your Gender'female/male': ")


if ( Gender == "female" ):
    age = int(input("enter your age : "))

    if ( 30 > age >=24):
        Graduation_state = input("enter your state'yes/no': ")


        if (Graduation_state == "yes"):
           print(" you are accepted ",Gender, " " , age )
        else:
           print(" you are rejected")

    else :
        print(" you are rejected")
else:
   
        print(" you are rejected")