
# explanation
# x = 1729 % 10
# print(x)

# x = 172 % 10
# print(x)

# x = 17 % 10
# print(x)

# x = 1 % 10
# print(x)


n = int (input("please enter the number : ")) # interlize the counter (n) the user enter 

total = 0

while (n > 0):   # to check the counter 
    digit = n % 10 
    total += digit
    n = n // 10  # the condition to update the loop 
print(" the total of the number is equal to = " , total)    
