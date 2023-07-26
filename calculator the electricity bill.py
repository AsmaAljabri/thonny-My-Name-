# make a calculator the electricity bill where user add the numbers 
# user enter the number of units to calculacte their  charge per OMR

num_unit = float(input("enter your number of units: "))

# if the units are less then 100 no charge 
if (num_unit < 100 ):
    print(" no charge" )
# if the units are less then 200 and more then 100 then the number of unts multiple by 0.024 per unit
elif (200 >num_unit > 100 ):
    num_unit *= 0.024 
    print(" your bill =",num_unit)
# if the units are more then 200 then the number of units multiple by 0.047 per unit

elif (num_unit > 200 ):
    num_unit *= 0.047
    print(" your bill =",num_unit)

