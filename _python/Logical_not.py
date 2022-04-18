#Logical not operator[ not ] : It is a uniary operator. It reverse the result of the condition. It applies to one condition 
# Case1 : True -> False
# Case2 : False -> True
# If the condition is True , the 'not' operator returns False.
# If the condition is False , the 'not' operator returns True.

num1 = 10

res1 = not (num1 == 10) # (num1 ==10) will returns true and not operator reverse the actual result.
print(res1)

res2 = not (num1 == 0) # (num1 == 0) will returns false and not operator reverse the actual result.
print(res2)
