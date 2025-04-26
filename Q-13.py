#  Q13 Write a program that simulates a simple ATM. The user should be able to:
#  Check balance
#  Deposit money
#  Withdraw money (ensure the balance doesn't go negative) Use an if-else structure to handle the user's
# choices

print("1 - To check balance")
print("2 - To Deposit money")
print("3 - To withdraw money")

balance=10000;

choice=int(input("Enter you choice: "));

if(choice==1):
    print("Balance: ",balance);
if(choice==2):
    d=int(input("Enter amount to deposit: "))
    print("Balance after deposit:",balance+d);

if(choice==3):
    w=int(input("Enter amount to withdraw: "))
    if(w>=balance):
        print("Error: Insufficient balance!")
    else:
        print("Balance after withdraw:",balance-w);
    



