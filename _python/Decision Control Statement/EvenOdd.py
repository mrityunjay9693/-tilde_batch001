#Program to print whether a number is even or odd
odd = 13
number = int(input("Enter the number:"))

if(number % 2 == 0):  #number =15 -> number%2 : 15%2 : remainder =1 : for even : remainder ==0 // for odd : remainder!=0
    print("Number is even")
else:
    print("number is odd")

