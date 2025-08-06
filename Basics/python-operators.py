"""comprehensive sample problem that will help you recall and use all major types of Python operators, including:

1. Arithmetic operators (+, -, *, /, **, %, //)
2. Assignment operators (=, :=, +=, -=, *=, /=, %=, //=, **=, ...., &=, |=, ^= : biwise-xor, >>=, <<=)
3. Comparison operators (==, !=, >, <, >=, <=)
4. Logical operators    (and , or, not)
5. Bitwise operators    ( &, |, ^ : XOR, ~, <<, >>)
6. Identity operators   (is, is not) : used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location
7. Membership operators (in, not in) : used to test if a sequence is presented in an object

🧠 Problem: Python Operator Mastery

a = 10
b = 5
c = [1, 2, 3, 4, 5, 10]
d = 0b1010  # binary for 10
e = 0b0101  # binary for 5

✅ Task: Write a function operator_practice(a, b, c, d, e) that:

1. Performs arithmetic operations and stores:
    - sum, difference, product, quotient, modulus, exponentiation, floor division.

2. Uses assignment operators to modify a variable:
    - Start with x = a, then successively apply +=, -=, *=, /=, %=, **=, //=

3. Compares a and b using all comparison operators (==, !=, >, <, >=, <=)

4. Applies logical operators (and, or, not) on some comparison results.

5. Applies bitwise operations between d and e:
    - AND, OR, XOR, NOT (on d), left shift, right shift.

6. Checks membership and identity:
    - Is a in c?
    - Is a not in c?
    - Does a is b?
    - Does a is not b?

7. Return all results in a dictionary for inspection.

Author: Nithusikan T.
Email : e19266@eng.pdn.ac.lk
Date  : 06/08/2025
"""

def operator_practice(a, b, c, d, e):
    # Task 01
    sum = a + b
    print(f"Sum: {sum}")

    difference = a-b
    print(f"Difference: {difference}")

    product=a*b
    print(f"Product: {product}")

    quotient=a/b
    print(f"Quotient: {quotient}")

    modulus=a%b
    print(f"Modulus: {modulus}")

    exponentiation=a**b
    print(f"Exponentiation: {exponentiation}")

    floor=a//b
    print(f"Floor division: {floor}")

    # Task 02
    x=a
    x+=2
    x-=3
    x*=5
    x/=2
    x%=5
    x**=3
    x//=2
    print(f"Final value of x: {x}")

    # Task 03
    x=a==b
    print(f"x is: {x}")
    y=a!=b
    print(f"x is: {x}")
    x=a>b
    print(f"x is: {x}")
    x=a<b
    print(f"x is: {x}")
    x=a>=b
    print(f"x is: {x}")
    x=a<=b
    print(f"x is: {x}")

    # Task 03
    f = x and y
    print(f"f is: {f}")
    g = x or y
    print(f"g is: {g}")
    h =  not f
    print(f"h is: {h}")
    
    # Task 04
    print(d & e)
    print(d | e)
    print(d ^ e)
    print(~d)
    print(a>>2)
    print(b<<1)
    
    # Task 05
    print(a in c)
    print(a not in c)

    print(a is b)
    print(a is not b)

if __name__ =="__main__":
    a = 10
    b = 5
    c = [1, 2, 3, 4, 5, 10]
    d = 0b1010  # binary for 10
    e = 0b0101  # binary for 5
    operator_practice(a, b, c, d, e)





