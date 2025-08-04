"""Type Casting and Checking

- Any type of data can be converted to string(str)
- But if we want to convert a string to other types, it must be transferable to that specific type
- ex: string 10.5 cannot be converted to int, it can be converted to float.
"""

# String to Other Types
a="10"
b="10"
c=a+b
print("Value of c is: ", c)
print("Type of a: ", type(a))
print("Type of b: ", type(b))
print("Type of c: ", type(c))
print("\n")

d=int(a)
e=int(b)
f=d+e
print("Value of f is: ", f)
print("Type of d: ", type(d))
print("Type of e: ", type(e))
print("Type of f: ", type(f))
print("\n")

g="10.5" # Can be converted to float not to int
# h=int(g) # Wrong
h=float(g)

# Other Types to String
a_=str(a)
b_=str(g)
c_=str(True)

print(f"a_ is {a_} is of type {type(a_)}")
print(f"b_ is {b_} is of type {type(b_)}")
print(f"c_ is {c_} is of type {type(c_)}")

