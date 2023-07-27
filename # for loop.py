# for loop 

stateName = "Virginia"
for letter in stateName :
    print(letter)

print("-----------------------------------------------")
print("-----------------------------------------------")

for i in range (1,6) :
    print(i, end ="  ")


print("-----------------------------------------------")

n = 6     #define the n  for the nested loop for 
for i in range (1,6):
    for i in range ( 1 , n):
        print(i, end = "  ")

    print(" ")
    n -= 1 

print("-----------------------------------------------")

for x in range (1,11):
    for n in range (1,5):
        print( x **n, end ="  ")
    print("  ")


print("-----------------------------------------------")

"""
define the n  for the nested loop for 

to draw 
*
* *
* * *
* * * * 
"""

n = 1     
for i in range (1, 5):
    for i in range ( n ):
        print("*", end = "  ")

    print(" ")
    n += 1
    
print("-----------------------------------------------")

n = 1     
for i in range (1, 6):
    for i in range ( n ):
        print("*", end = "  ")

    print(" ")
    n += 1
n = 6    
for i in range (0, 6):
    for i in range ( n ):
        print("*", end = "  ")

    print(" ")
    n -= 1