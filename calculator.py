"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example

import math

def square_root(a):
    if a < 0:
        raise ValueError("Cannot take the square root of negative number")
    else:
        return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b): 
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if a == 0:
        raise ZeroDivisionError("Denominator cannot be negative")
    else:
        return b / a

def logarithm(a, b): # use math library/raise ValueError
    try:
        math.log(b, a)
    except ValueError:
        print("Log Error")

def exponent(a, b):
    return a ** b

