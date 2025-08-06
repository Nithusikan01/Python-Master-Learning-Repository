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
print(mytripler(10))

# pass args in single line
print(myfunc(4)(10))

