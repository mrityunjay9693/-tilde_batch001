#Logical OR Operator[ or ] : It has two operands. It is a binary Operatror. Returns 'true' if either one of the Operands is true
#true or false = true
#true or true  = true
#false or true = true
#false or false = false 
num1 = 20
num2 = 30

# case 1 : true or false = true
print("Case 01 :  true or false = true")
res1 = (num1 == 20) or (num1 == num2) # true or false ,returns : true 
print(res1)

# case 2 : true or true = true
print("Case 02 :  true or true = true")
res2 = ( num1 == 20 ) or ( num2>num1 ) # true or true ,returns : true 
print(res2)

# case 3 : false or true = true
print("Case 03 :  false or true = true")
res3 = ( num1 == 30 ) or ( num2>num1 ) # false or true ,returns : true 
print(res3)

# case 4 : false or false = false
print("Case 04 :  false or false = true")
res4 = ( num1 >= 30 ) or ( num2 <= num1 ) # false or false ,returns : false 
print(res4)
