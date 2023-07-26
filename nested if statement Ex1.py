# nested if statement 


state = input("enter your state'yes/no': ")
age = int(input("enter your age : "))


if ( age >= 18):
    
    if ( state == "yes"):
        print(" Graduated and the age is",age, " years old" )
    else :
        print(" Not Graduated and the age" ,age, " years old")
else:
    print( "the age is under 18 years old " )