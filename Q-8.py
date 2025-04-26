'''  Write a program that checks if a username and password entered by the user match the pre-set values
 username = "admin" and password = "1234". If both match, print "Login Successful", otherwise print
 "Login Failed".'''
 
user="admin"
password=1234
name=input("Enter you Username: ")
pas=int(input("Enter your password: "))

if(name==user and pas==password):
    print("Login Successfull !")
else:
    print("Login Failed !")
    
    

