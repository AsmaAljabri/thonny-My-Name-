"""
printing the perfact number between the numbers 1 to 100 
using the nested loop by using for loop 
"""
print(" the perfect number btween 1 to 100 ")

for i in range (1,101):
    per_num = 0 

    for x in range (1, i):
        if (i % x == 0):
            per_num += x 

    if per_num == i :
        print(i, "it is the perfect number")