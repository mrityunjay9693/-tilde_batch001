number1 = float(input("Enter first number: "))   # 18
number2 = float(input("Enter second number: ")) #2


if(number2): #  "non-zero" value returns true and "zero" value returns false
    remainder = number1 % number2   # returns remainder
    quotient = number1 / number2 # returns quotient
    print("remainder: ",remainder)
    print("quotient: ",quotient)
else:
    print("Division by 0 not posiible. Try again!")
    

