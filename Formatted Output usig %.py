"""
Formatted Output: String Format Operator using % 10 s for space
"""
Name = input ( "please enter your name " )	
Age = int(input ( "please enter your Age " ))

# the output will result to be your name and have 10 space  that are stored in the memory 
print(" user name %10s" %(Name) )

print(" user age %3*d" %(Age))

