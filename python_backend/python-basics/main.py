# How Python Works?
# Python code files are read line by line by the Python Interpreter, Interpreter convert this code into Byte-code which is close to the machine code then this machine code is executed by the cpython Virtual Machine this how our program runs on Machine.


# username = input("Enter your username: ")
# print(f"Hello: {username}")


# Data-Types in Python

# These are the fundamental datatypes in Python
# int
# float
# complex
# str
# bool
# list
# set
# tuple
# dict


# classes -> custom types
# Specialized Data Types like Modules

# Another Data Type is:- 
# Complex

# None -> Type 
# print(round(4.7))
# print(round(4.3))
# print(abs(-78))


# Operator Precedence -> PEMDAS
# print((20-3) + 2 ** 2) # 21 -> o/p


#  All these Integers and Strings are stored as binary in memory now to convert them into binary
# bin Method -> bin()
# print(bin(78))


# Variables in the python
# variables are containers which are used to store some Information.

num1,num2,num3 = 78,19,356
# print(num1,num2,num3)

# Expressions vs Statments

# Expression :- A piece of code which produces result or value.
# Statement:- whole line of code is called statement whether it produces result or not. A statement is a complete instruction which Python can execute. such as assigning a value to the variable or calling the function.

# "Expressions are a combination of programming logic that evaluates to a result. Statements are more general building blocks... It's common to include expressions within statements but not vice versa."

# iq = 25 + 5
# code = iq * 19

# Augmented Assignment Operator
count = 0

count += 25
# print(count)

# String In Python

username = 'Supercoder'
password = 'supersecret'
long_string = """
  Hello, I ams Arpit,
  I am from India
"""
# print(long_string)
# first_name = 'Arpit'
# last_name = 'Mishra'
# print(first_name + ' ' + last_name)


# String Concatenation
# format()

# print("Hello, My name is {} and I am {} years old!".format("Arpit",25))

# Escape Sequence
greeting_string = "\t It\'s Kind of \"Sunny\" day \n in the UK"
# print(greeting_string)


# String positions can be accessed using Indexes
# Strings are Immutable.

# Built In Methods In Strings
# len()
# upper()
# lower()


quote = 'to be or not to be!'
# print(quote.upper())
# print(quote.capitalize())
# print(quote.lower())
# print(quote.find('be'))
# print(quote.replace('be','me'))

