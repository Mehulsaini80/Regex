#Write a program that takes three numbers as input and prints the largest of the three.

a=int(input("Enter a: ")); 
b=int(input("Enter b: ")); 
c=int(input("Enter c: ")); 

if(a>b and a>c):
    print("A is largest !");
elif(b>a and b>c):
    print("B is largest !");
else:
    print("C is largest !");
