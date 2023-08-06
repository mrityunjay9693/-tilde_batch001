#program to illustrates a nested-if

number = int(input("Enter a number: "))

if(number==0):
    print("Number is zero. Provide a non-zero value")
else:    
    if(number):  #non zero returns true., Zero returns false
    
        if(number%2==0):  
            print("Inner if works")
        else:
            print("Inner if condition becomes false. Number is not equal to 10")
if(number>20):
    print("Number is greater than 20")
    
        