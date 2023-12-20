""" Python Variables """

# Basic syntax of creating a variable
name = "John"  # Variable of type String (str)
age = 35  # Variable of type Integer (int)


# Casting variables
x = str(3)  # x will be '3' of type String (str)
y = int(3)  # y will be 3 of type Integer (int)
z = float(3)  # z will be 3.0 of type Float (float)


# Get the type of a variable
print(type(x))  # <class 'str'>
print(type(y))  # <class 'int'>
print(type(z))  # <class 'float'>


# Creating strings in python
x = "John"
# is the same as
x = "John"
# is the same as
x = """John"""


# Variables in python are case-sensitive
apple = 4
# is not the same as
Apple = "Sally"


# Variable names can contain letters, numbers, and underscores
# Allowed variable names:
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"
# Not allowed variable names:
# 2myvar = "John"
# my-var = "John"
# my var = "John"


# Assign multiple values to multiple variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)  # Orange
print(y)  # Banana
print(z)  # Cherry
x = y = z = "Orange"
print(x)  # Orange
print(y)  # Orange
print(z)  # Orange
# Unpack a collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)  # apple
print(y)  # banana
print(z)  # cherry


# Output variables
x = "awesome"
print("Python is " + x)  # Python is awesome
x = "Python is "
y = "awesome"
z = x + y
print(z)  # Python is awesome
x = 5
y = 10
print(x + y)  # 15


# Global variables
x = "awesome"


def myfunc():
    print("Python is " + x)


myfunc()  # Python is awesome
