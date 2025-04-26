''' Q9 Write a program that takes three sides of a triangle as input and checks if those sides form a valid
 triangle. A triangle is valid if the sum of any two sides is greater than the third side.
 Check conditions like a + b > c, b + c > a, and a + c > b'''
 
a=1
b=2
c=3

if(a+b>c or b+c>a or a+c>b  ):
    print("Triangle")
else:
    print("Not a Triangle")
    