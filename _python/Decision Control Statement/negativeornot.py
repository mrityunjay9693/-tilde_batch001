# Program to print whether a number is entered is negative or not
number = int(input("Enter the number:"))

if(number < 0):    # number = 8 < 0 : negative // number = 8 >=0 : positive
    print("number is negative")
else:
    print("number is not negative. Its positive")