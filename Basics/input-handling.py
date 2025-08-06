"""Input Handling
Add 2 numbers
 - get the 2 numbers as user inputs

Author: Nithusikan T.
Email : e19266@eng.pdn.ac.lk
Date  : 06/08/2025
"""
def add():
    a=int(input("Enter the 1st number: "))
    b=int(input("Enter the 2nd number: "))

    print(f"The sum is {a+b}")

if __name__ == "__main__":
    add()

"""
input() function needs manual intervention.
- cannot be used when we use schedulers.
- need to use sys library.
"""