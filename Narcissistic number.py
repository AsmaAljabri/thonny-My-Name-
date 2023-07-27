

# Take the input number as an string 
# Convert the number to a integer 
# Calculate the number of digits in the number example : 153 = 1*3+ 5*3 + 3*3= 153 = nar num
# 153 % 10 = 3 ----> 153//10 = 15 and the loop star  again and add t to the sum 


number = input("enter the number")

num = int(number)

sum = 0

ans = num

while(num != 0):

    digit = num % 10
    sum +=  digit ** (len(number) ) # Calculate the sum of each digit raised to the power of the number of digits
    num = num // 10 
if(sum == ans):    # Compare the result with the original number
    print(" yes")
else:
    print(" no ")    

