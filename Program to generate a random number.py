# Program to generate a random number between 0 and 9

# importing the random module
# import random



import random

y = random.randint(0,10)
x = random.randint(0,10)

while 1 :
    x = random.randint(0,10)  # the program generate any 2 numbers
    y = random.randint(0,10)  
    
    print( x ," + ",y, " = " )
    z = x + y
    ans = input ("what is the answer for the sum of y and x") # the user need to write the sum of the numbers
    print(ans)
    if ( ans != " done"): # using If else statement to check if the answer is correct or not unless the user enter "done " the loop will end
        if ( int(ans) ==  z  ):
            print("the answer is correct")
        else:
            print(" the answer is not correct")
 
    else:
        break
