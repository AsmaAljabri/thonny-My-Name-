# make program to compare between two times what time will come first using 24h
# user enter the first and second time hours and minets


hour_of_FirstT= int(input("enter the hour of the first time 24h:  "))
min_of_FirstT= int(input("enter the minets of the first time :  "))

hour_of_secondT= int(input("enter the hour of the second time 24h :  "))
min_of_secondT= int(input("enter the minets of the second time :  "))

if ( hour_of_FirstT < hour_of_secondT):
    print( hour_of_FirstT,min_of_FirstT, " is the come first")
     
else:
    
    if ( hour_of_FirstT == hour_of_secondT):
        
        if ( min_of_FirstT <= min_of_secondT ):
            print( hour_of_FirstT,min_of_FirstT, " is the come first")
        else:
            print( hour_of_secondT,min_of_secondT, " is the come first")
    else:
        print( hour_of_secondT,min_of_secondT, " is the come first")
        