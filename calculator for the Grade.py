# make a prgram to calculator for the Grade where user will enter their grade and the output will define their result using compound if else statement 

Grade = float(input("enter your Grade: "))


if (Grade > 90 ):
    print("A" )
elif (80 < Grade <= 90 ):
    print("B" )
elif (60 <= Grade <= 80):
    print("C" )
elif (60 < Grade):
    print("D" ) 
else:
    print("Faild")

