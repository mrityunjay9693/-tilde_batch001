#Relationals Operators or Comparison Operator : >, <, ==, !=, >=, <=
#Expression : combination of operator and operands to generate some result.
num1 = 5  # assignment expression , here 5 is assigning to the variable num1 and 1 is assigning to variable num2.  
num2 = 1  
num3 = 5
# Greater than relational Operatror ( > ) : It has two operands. Returns 'true' ,if left operand greater than right operand 

res1 = num1 > num2

#Result for Greater than operation
print("Result for Greater than")
print(res1)

# Less than relational Operatror ( < ) : It has two operands. Returns 'true' ,if left operand less than right operand.

res2 = num1 < num2 #true 5<1
#Result for Less than operation
print("Result for Less than :")
print(res2)

# Equal to relational Operatror ( == ) : It has two operands. Returns 'true' ,if both the operands are equal.

res3 = num1 == num2 # 5==1 : false  Binary operands : two operands
res4 = num1 == num3 # 5 == 5 :true
#Result for Equal to Operation
print("Result for Equal to :")
print(res3, res4)

# Not Equal to relational Operatror ( != ) : It has  two  operands. Returns 'true' ,if both the operands are not equal.

res5 = num1 != num2  # num1(5) != num2(1) = true
res6 = num1 != num3  # 5 != 5 = false

#Result fore Not equal to
print("Result for Not equal to :")
print(res5, res6)

# Greater than or Equal to relational Operatror ( >= ) : It has two operands. Returns 'true' ,if either left operands greater than or equal to the right operands.
#  4 >= 1 = true
#  1 >= 1  = true
#  5 >= 7 = false
#num1 = 5   
#num2 = 1  
#num3 = 5
res7 = num1 >= num2  # 5 >= 1 : true
res8 = num2 >= num1 # 1 >= 5  : false
res9 = num1 >= num3  # 5 >= 5 : true

#Result for Greater than equal to
print("Result for Greater than equal to :")
print(res7, res8, res9)

# Less than or Equal to relational Operatror ( <= ) : It has two operands. Returns 'true' ,if either left operands less than right operands or equal to the right operands.
#  1 <= 4 = true
#  1 <= 1  = true
#  10 <= 7 = false
#num1 = 5   
#num2 = 1  
#num3 = 5
res10 = num1 <= num2  # 5 <= 1 : false
res11 = num2 <= num1  # 1 <= 5 : true
res12 = num1 <= num3  # 5 <= 5 : true

##Result for Less  than equal to
print("Result for Less than equal to :")
print(res10, res11, res12)

#50 questions

