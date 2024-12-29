#Logical Operator in Python

num1 = 5
num2 = 10
num3 = 15

#And Operator
AndOp = (num1 < num2) and (num2 < num3)
print(AndOp)

#Or Operator
OrOp = (num1 > num2) or (num3 > num1)
print(OrOp)

#Not Operator
NotOp = not(num1 > num2 and num2 > num3)
print(NotOp)