# calculate the area of the given shape 

from math import *

PI = 3.14

"""ask the user for the inputs in order to calculate the gap area beween
the circale and the square and add the area of the triangle,
NOTE: that from the shape the Lenght is equal to 4 and the hight is equal to 5
where the shape is consider of the house shape that has square and triangle and
and there is circle inside of the square that where the r is equal to the length = 4

"""
L = int ( input ( " Enter the lenght"))
h = int ( input ( " Enter the hight"))
# the calculate the area of the square 
square_A = ( 4 * L )
# the calculate the area of the triangle  
triangle_A =  (L/2) *h
# the calculate the area of the circle  
circle_A = PI * ((L/2) ** 2)
# calculate the full area the gap + triangle area 
full_area = ( square_A - circle_A) + triangle_A

print("the full area =", full_area )

