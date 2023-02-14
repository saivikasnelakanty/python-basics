def sub(num1, num2):
    result = num1 - num2
    return result
subtraction = sub(10,2)
print(subtraction, type(subtraction))

def div(num1, num2):
    result = num1 / num2
    return result
division = div(25,5)
print(division, type(division))

a = 5
from numpy.random import randn
data = {i : randn() for i in range (7)}
print(data)
