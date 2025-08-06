"""
- Need to use sys library
- Need to run using terminal for giving arguments.

Author: Nithusikan T.
Email : e19266@eng.pdn.ac.lk
Date  : 06/08/2025
"""
import sys

if len(sys.argv) < 3:
    print("Usage: python file_name.py first_name last_name")
    sys.exit()

first_name = sys.argv[1]
last_name = sys.argv[2]

full_name_list = sys.argv[1:] # will provide a list of string
full_name = "".join(sys.argv[1:]) # a single string
# Format the name
email = first_name.lower() + last_name.lower() + "@company.com"

# Output
print("---- Your Email ----")
print(f"Email: {email}")
print(sys.argv[0])
print(full_name_list)
print(full_name)