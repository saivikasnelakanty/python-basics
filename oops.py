# fruits = ["grapes", "mango", "watermelon"]
# names = ["kiran", "mohit"]
# age = [23, 34]
# marks = [67, 78, 89]
# emp_vikas = {"name" : "vikas", "age" : 23, "fruit" : "grape", "marks" : 89}
# emp_vijay = {"name" : "vijay", "age" : 26, "marks" : 98, "fruit" : "mango"}
# emp_rahul = {"name" : "rahul", "age" : 26, "marks" : 98}
# emp_laxman = {"name" : "laxman", "age" : 26, "mark" : 98}
# print(emp_vikas["fruit"])
# print(emp_vijay["fruit"])
# print(emp_rahul["fruit"])
# emp_mohit = ["mohit", 23, "watermelon", 89]
# emp_kiran = ["kiran", 23, 89, "watermelon"]
# print(emp_mohit[2])
# print(emp_kiran[3])

#Template
class Employee:
    def __init__(self, name, age, marks, fruit):  #dunder methods (shortcut is "__")
        self.name = name
        self.age = age
        self.marks = marks
        self.fruit = fruit

    def get_name(self):  
        return self.name + "_zenoti"
    
    def get_grade(self):
        if self.marks >= 60:
            return("A")
        else:
            return("B")

    def get_fruit_juice(self):
        return(self.fruit) + "_juice"

emp_vikas = Employee("vikas", 25, 50, "watermelon")
# print(emp_vikas.name)
print(emp_vikas.name, emp_vikas.marks, emp_vikas.fruit, emp_vikas.age)

emp_raja = Employee("vijay", 27, 87, "mango")
print(emp_raja.name, emp_raja.marks, emp_raja.fruit, emp_raja.age)
print(emp_vikas.get_name())
print(emp_vikas.name)
print(emp_vikas.get_grade())
print(emp_raja.get_grade())
print(emp_vikas.get_fruit_juice())