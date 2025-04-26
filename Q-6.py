#Write a basic calculator program that takes two numbers and an operator (+,-, *, /) as input and
# performs the specified operation. Print the result based on the operation.

a=int(input("Enter 1st number: "));
b=int(input("Enter 2nd number: "));
o=input("Enter Operator: ");

if(o=="+"):
    print("Addition:",a+b)
elif(o=="-"):
    print("Subraction:",a-b)
elif(o=="*"):
    print("Multiplication:",a*b)
elif(o=="/"):
    print("Divide:",a/b)
    
