''' 
Write a program that takes a percentage (integer) as input and prints the corresponding grade based
 on the following criteria:
 >= 90: Grade A
 >= 80: Grade B
 >= 70: Grade C
 >= 60: Grade D
 < 60: Grade F
'''

per=int(input("Enter Percentage: "));

if(per<=60):
    print("Grade F");
elif(per>=60 and per<70):
    print("Grade D");
elif(per>=70 and per<80):
    print("Grade C");
elif(per>=80 and per<90):
    print("Grade B");
elif(per>=90):
    print("Grade A");
