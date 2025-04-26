'''Q11 Write a program that calculates the discount for a product based on its price:
 If price is greater than 1000, discount is 10%
 If price is between 500 and 1000, discount is 5%
 Otherwise, no discount
 Print the final price after applying the discount'''
 
price=int(input("Enter Product Price: "));

if(price>1000):
    print("Discount is 10%");
    print("Final price is: ",price-price*10/100)
elif(price>=500 and price<=1000):
    print("The discout is 5% ");
    print("Final price is: ",price-price*5/100)
else:
    print("NO Discount !");