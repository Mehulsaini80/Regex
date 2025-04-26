#Write a program to check if a given year is a leap year. A leap year is divisible by 4 but not by 100
# unless it is also divisible by 400

year=1944;

if(year%400!=0):
    if(year%4==0 and year%100!=0):
        print(year,"is a leap year");
    else:
        print(year,"is not a leap year");
else:
    print(year,"is not a leap year");