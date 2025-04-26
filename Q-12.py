'''Q12 Write a program that takes the name of a month as input and prints the number of days in that
 month. Consider leap years for February.'''
 
m=input("Enter month: ");

if(m=="jannuary" or m=="march" or m=="may" or m=="july" or m=="agust" or m=="october" or m=="december"):
    print("31 Days")
    
elif(m=="februry"):
    print("28 days")
    
else:
    print("30 days");
 