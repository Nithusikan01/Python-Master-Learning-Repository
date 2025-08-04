"""Scope of Python Variables.

# 4 types of scopes
1. Local (L)      : Within a function or a block
2. Enclosing (E)  : Within parent function and the inner function/s 
3. Global (G)     : Within the file itself
4. Built-In (B)   : Python scope

# Order of scope
L --> E --> G --> B
"""

travel_partner="pickme" # G

def ride():
    vehicle="bike" # E

    def book_now():
        quantity=1 # L
        print(f"Booking {quantity} {vehicle} using {travel_partner}.")
    book_now()


ride()
print(f"This is the {__name__} file.") # __name__ : # B - Python scope
