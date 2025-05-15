def total(num1,num2):
    """
    Take two arguments ang give total of two numbers.
    :param num1:
    :param num2:
    :return:
    """

    return num2 + num1

result = total(78,25)
# print(f"Result of two numbers are: {result}")

# *args and **kwargs in python
# *args -> to help get any number of arguments
# **kwargs -> to get any number of keyword arguments
def super_func(*args,**kwargs):
    print(kwargs)
    return sum(args)

# print(super_func(1,2,3,4,5,6,student_name="Harry Potter",house="Gryffindor",school_name="Hogwarts"))

#order of function:- parameters,args then kwargs

# Exercise:- highest even

def highest_even(*args):
    largest_even = None
    for number in args:
        if number % 2 == 0:
            if largest_even is None or largest_even < number:
                largest_even = number
        else:
            continue

    return largest_even

result = highest_even(10,2,3,4,8,11,95)
# print(f"Largest Even Number is: {result}")


# Walrus Operator

a = 'hellooooooooooooooo'

if (n:= len(a)) > 14:
    print(f"The length of string is greater than 5: {n} ")


# Scope In Python :- what variables do i have access for. Scope in Python has functional scope

if True:
    x = 10

# print(x) -> scope is only created when we create a function.


# Scope Rules
# 1. Start with local
# 2. Parent local?
# 3. look into Global
