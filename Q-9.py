''' Q9 Write a program that takes three sides of a triangle as input and checks if those sides form a valid
 triangle. A triangle is valid if the sum of any two sides is greater than the third side.
 Check conditions like a + b > c, b + c > a, and a + c > b'''
 
a=int(input("Enter side 1: "));
b=int(input("Enter side 2: "));
c=int(input("Enter side 3: "));

if(a+b>c and b+c>a and a+c>b  ):
    print("Triangle")
else:
    print("Not a Triangle")
    
