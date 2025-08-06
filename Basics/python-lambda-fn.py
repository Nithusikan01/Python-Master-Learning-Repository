"""
A lambda function is a small anonymous function.
A lambda function can take any number of arguments, but can only have one expression.
"""

x = lambda a : a + 5
print(x(4))

y = lambda b, c,  d: b * c + d

z = y(3, 4, 5)
print(z)

print(f"Type of z: {type(z)}")
print(f"Type of y: {type(y)}")

# The power of lambda is better shown when you use them as an anonymous function inside another function.
# Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:

def myfunc(n):
    return lambda a : a * n

mydoubler = myfunc(2)
print(mydoubler(10))

mytripler = myfunc(3)
print(mytripler(10))

# pass args in single line
print(myfunc(4)(10))

