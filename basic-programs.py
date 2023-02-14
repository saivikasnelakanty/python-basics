# Variables
name = "vikas" # String Value
salary = 23000 # Integer Value
marks = 45.3 # Float Value
male = True # Boolean Value
print(name, salary, marks, male)

# Conditional Statements
if salary > 20000:
    print("Taxable Income.")
elif salary < 20000 and salary > 10000:
    print("Rebate will be applied.")
else:
    print("Not Taxable.")

# Loops
# For Loop
for i in range(4):
    print(i)

# while loop
i = 0
while i < 4:
    print(i)
    i += 1

# List
fruits = ["Orange", "Mango", "Grapes"]
print(fruits)
fruits.append("watermelon")
print(fruits)

# Dict
employee = {"name":"vikas", "age":25, "salary":30000}
print(employee)
print(employee["age"])