#var = -86.05
#float_number = -234.567
#print("The Absolute of integer is ", abs(var))
#print("The Absolute value of floating number is ", abs(float_number))

#complex_number = (3 - 4j)
#print("Absolute value or magnitude of complex is:", abs(complex_number))

#Time-Distance calculation using python abs()
#Distance = Speed * Time
# Speed = Distance / Time
# Time = Distance / Speed

#def cal_speed(Distance, Time):
    #Speed = Distance * Time
    #print("Distance(KM) = ", Distance)
    #print("Time (hr) = ", Time)
    #print("Speed is ", Speed)
    #return
#cal_speed(23, 56)
# print("The Calculated Speed is ", cal_speed(23, 56))

#Function to calculate speed
def cal_speed(Distance, Time):
    print("Distance(KM) : ", Distance)
    print ("Time(HR) :", Time)
    return Distance / Time

#Function to calculate distance traveled
def cal_dis(Speed, Time):
    print("Speed(KM/HR) :", Speed)
    print("Time(Hr) :", Time)
    return Speed * Time

#Function to calculate the time taken
def cal_time(Distance, Speed):
    print("Distance(KM) :", Distance)
    print("Speed(KM/HR) :", Speed)
    return Distance / Speed

#Calling a Functions
print("The Speed is ", cal_speed(34, 45))
print("The Distance is ", cal_dis(45, 46))
print("The Time is ", cal_time(46, 47))


# python all() function

#All elements of list are true
l = [4,5,1]
print(all(l))

#All elements of list are flase
l = [0,0,False]
print(all(l))

#Some elements of list are
# True while others are flase
l = [1,0,6,7,False]
print(all(l))

#Empty List
l = []
print(all(l))


# Example 2: working of all() with tuples
# Here we are considering a tuple as a iterable.
# All elements of tuple are true
t = (2, 4, 6)
print(all(t))

# All elements of tuple are false.
t = (0, False, False)
print(all(t))

#Some elements of tuple
#are true while others are false
t = (5, 0, 3, 1, False)
print(all(t))

# Empty tuple
t = ()
print(all(t))


#Python any() Function:
# All elements of list are True
l = [4,5,6]
print(any(l))

#All elements of list are False
l = [4,5,6,False]
print(any(l))

#Some elements of list are true while others are false
l = [1,0,6,7,False]
print(any(l))

#Empty list
l = []
print(any(l))
print("----------")
# Example 2: Working of any() function with Tuples
# Use of any() function on python tuples
# All elements of tuple are true
t = (2,4,6)
print(any(t))

#All elements of tuple are false
t = (5, 0, 3, 1, False)
print(any(t))

#Empty tuple
t = ()
print(any(t))
print("-----------")

#Example: Working of any() function with sets
# All elements of sets are true
s = {1, 1, 3}
print(any(s))

# All elements of set are false
s = {0, 0, False}
print(any(s))

# Some elements of set are true while others are false
s = {1, 2, 0, 8, False}
print(any(s))

#Empty set
s = {}
print(any(s))
print("---------")

#Example 4: Working of any() function with dictionaries
#Note: In case of 


print(ascii('¥'))
print("-------------------------")

# Example 2: Python ascii() on new line characters
# Here we take a varaiable with multiline string and pass it into the ascii() and it returns "\n", the value of new line is "\n".

test_str = '''Geeks
for
geeks'''
print(ascii(test_str))
print("------------------")

#Example 3: Using Python ascii() on Set, List, and Tuple
# Below example shows how to use Python ascii() on python Set, List, Tuple.

# Python ascii() on set
test_set = {"Š", "E", "T"}
print("ascii on python set: ", ascii(test_set))

# Python ascii() on List
test_list = ["Ň", "ĕ", "Ŵ"]
print("ascii on python list: ", ascii(test_list))


# Python ascii() on Tuple
test_tuple = ("Ģ", "Õ", "Õ", "D")
print("ascii on python tuple: ", ascii(test_tuple))

print("-----------------------")

num = 100
print(bin(num))

print(100 * "-")


#Python bool() Function Example:
# Python program to illustrate
# built - in method bool()

# Returns False as x is  False
x = False
print(bool(x))

# Returns True as x is True
x = True
print(bool(x))

# Returns False as x is not equal to y
x = 5
y = 10
print(bool(x == y))

# Returns False as x is None
x = None
print(bool(x))

# Returns False as x is an empty sequence
x = ()
print(bool(x))

#Returns False as x is an empty mapping
x = {}
print(bool(x))

#Returns False as x is 0
x = 0
print(bool(x))

# Returns True as x is a non empty string
x = "vikas"
print(bool(x))

print(50 * "-")
#bool() in python input
# Here we take input in boolean (True/False) in boolean type with bool() function and check whether it is returned true or false.

# user_input = bool(input("Are you hungry? True or False: "))
# if user_input == "Ture":
# print("You need to eat some foods")
# else:
   # print("Let's go for a walk")
    

print(70 * "-")

#Python bytearray() function
#Code 1
str = "vikas"
array_1 = bytearray(str, 'utf-8')
array_2 = bytearray(str, 'utf-16')

print(array_1)
print(array_2)

print(70 * "-")

#Code 2 if an integer, creates an array of that size and intialized with null bytes.

# size of array
size = 3

# will create an array of given size
# and intializes with null bytes

array1 = bytearray(size)

print(array1)

print(70 * "-")

#Python bytes() method: Converts an object to an immutable byte-represented object of given size and data.
# Syntax: bytes(src, enc, err)

#Python callable() function: In general, a callable is something that can be called. This buit-in method in python checks and returns True if the object is passed appers to be callable, but may not be, otherwise False.
# Syntax: callable(object)

#The callable() method takes only one argument, an object and returns one of the two values.
# Returns True, if the object appears to be callable.
# Returns False, if the object is not callable.

# Note: There may be few cases where callable() returns true, but the call to object fails. But if a case returns False, calling object will never suceed.


#Python chr() in python:
# The python chr() function returns a string from unicode code integer.
# Python chr() function syntax:
# Syntax: chr(num)
# num: an unicode code integer
# Retun: Returns String

# Example:
print(chr(97))
print(70 * "-")

#Suppose we want to print 'GeeksforGeeks'
print(chr(71), chr(101), chr(101), chr(107), chr(115), chr(32), chr(102), chr(111), chr(114), chr(32), chr(71), chr(101), chr(101), chr(107), chr(115))

# Printing character for ech unicode ineger in number list.
numbers = [17, 38, 79]
for number in numbers:
    letter = chr(number)
    print("character of ASCII value", number, "is", letter)

# what happens if we give something out of range?
print(chr(400))
print(70 * "-")

# Python classmethod() in python
# The classmethod() is an inbuilt function in python, which returns a class method for a given function:
# Syntax: classmethod(function)
# Parameter: This function accepts the function name as a parameter.
# Return Type: This function returns the converted class method.
# You can also use @classmethod decorator for classmethod definition.

# Syntax:
# @classmethod
#   def fun(cls, arg1, arg2, ....):
# Where,
# fun: The function that needs to be converted into a class method.
# Returns: A class method for function.
# Classmethod() method are bound to a class rather than an object. classmethods can be called by both class and object. These methods can be called with a class or with an object.

#Class Method vs Static Method
# A class method takes cls as the first parameter while a static emthod needs no specific parameters.
# A class method can access or modify the class state while a static method can't access or modify it.
# In general, static methods know nothing about the class state. They are utility-type methods that take some

class geeks:
    course = 'DSA'

    def purchase(obj):
        print("Purchase course: ", obj.course)

geeks.purchase = classmethod(geeks.purchase)
geeks.purchase()


class student:
    name = "GeeksforGeeks"

    def print_name(obj):
        print("The name is: ", obj.name)

student.print_name = classmethod(student.print_name)
student.print_name()

#Example 3: Factory method using class method
# Uses of classmethod() function are used in factory design patterns where we want to call many functions with the class name rather than an object.

print("-" * 100)

# Python compile() function:
# The python compile() function takes source code as input and returns a code object which is ready to be executed and which can later be executed by the exec() function.
# Syntax: compile (Source, filename, mode, flags=0, don't_inherit=False, optimize=-1)
# Parameters:
#   Source: It can be a normal string, a byte string, or an AST object.
#   FileName: This is the file from which the code was read. If it wasn't read from a file, you can give a name yourself.
#   Mode: Mode can be exec, eval or single.
#           a.eval - If the source is a single expression.
#           b.exec - It can take a block of a code that has python statements, class and functions and so on.
#           c.single - It is used if consists of a single interactive statement.
#   flags(optional) and don't_inherit(optional) - Default value = 0. It takes care that which future statements affect the compilation of the source.
#   Optimize(optional) - It tells optimization level of complier. Default value -1.

#Python compile() function example.
# Example 1: Simple compile() example in python.
# Here filename is mulstring and exec mode allows the use of exec() method and the compile method converts the string to python code object.

#Creating sample sourcecode to multioly two variables x and y.
srcCode = 'x = 10\ny = 20\nmul = x * y\nprint("mul =", mul)'
exeCode = compile(srcCode, 'mulstring', 'exec')
exec(exeCode)

#Example: Another demonstration working of compile
a = compile('x', 'test', 'single')
print(type(a))
exec(a)

#Example: Another example, python compile function from file
# In this example, we will take main.py file with some string display methods, and then we read the file content and compile it to code the object and execute it.

# string = "Welcome to python course"
# print(string)
# f = open(file = 'C:\Users\saivikasn\OneDrive - Zenoti India Private Limited\Python\Python', mode = 'r')
# temp = f.read()
# f.close()

# code = compile(temp, 'C:\Users\saivikasn\OneDrive - Zenoti India Private Limited\Python\Python', 'exec')
# exec(code)


# Applications:
# 1: If the python code is in string form or is an AST object, and you want to change it to a code object, then you can use compile() method.
# 2: The code object returned by the compile() method can later be called using methods like exec() and eval() which will execute dynamically generated python code



# Python Complex() Function:
# The python complex() function returns a complex number (real + Imaginary) example (5+2j) when real and imaginary parts are passed, or it also converts a string to a complex number.
# Syntax: complex(real, imaginary)
#   parameters: real[optional]: numeric type(including complex). It defaults to zero.
