'''Q12 Write a program that takes the name of a month as input and prints the number of days in that
 month. Consider leap years for February.'''
 
m=input("Enter month: ");

if(m=="jannuary" or m=="march" or m=="may" or m=="july" or m=="agust" or m=="october" or m=="december"):
    print("31 Days")
    
elif(m=="februry"):

    year=int(input("Enter year: "));
    
    if(year%400!=0):
        if(year%4==0 and year%100!=0):
            print(year,"is a leap year");
            print("Februry: 29 days")
        else:
            print(year,"is not a leap year");
            print("28 days")
    else:
        print(year,"is not a leap year");
        print("28 days")
    
    
else:
    print("30 days");
 
