# make a program that calculator for the BMI and user enter the numbers 

weight = float(input("enter your weight in 'kg': "))
height = float(input("enter your height in 'cm': "))

# convert the height from CM to M

height = height/ 100

BMI = (weight / (height**2) )
print(BMI)

if (BMI < 18.5 ):
    print("underweight" )
 
elif (18.5 <= BMI < 25.0 ):
    print("Normal" )
    
elif (25.0 <= BMI < 30.0 ):
    print("overweight" )
    
else:
    print("obese")