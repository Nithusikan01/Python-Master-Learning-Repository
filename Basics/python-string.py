"""Python Strings

Author: Nithusikan T.
Email : e19266@eng.pdn.ac.lk
Date  : 06/08/2025
"""
student_name = 'hello world'

# Masking a string (Mobile number)
mobile = '1234567890'
masked_mobile = mobile[:2] + "******" + mobile[-2:]
print(masked_mobile)
print(student_name.title())

# upper(): makes all characters to upper case
print(student_name.upper())

# lower: makes all characters to lower case
print(student_name.lower())

# title(): makes the first letter in ecah word capital
print(student_name.title())
print(f"{student_name[0].upper() + student_name[1:6] + student_name[6].upper() + student_name[7:]}")

# replace(): replaces all the instance of a given character or word or sequence in a string
print(student_name.replace("hello world", "Hello"))
print(student_name.replace("world", "guys"))
print(student_name.replace("l", "*"))

# split(): splits a string on a given delemitter
# strip(): removes leading and trailing spaces
message="Your OTP is: 1234. Please don't share it with anyone."
otp=message.split(':')[1].split(".")[0].strip()
print(otp)

# in: membership operation
promo_msg="Use zomato100 to get 100 off on your first order."
if "zomato100" in promo_msg:
    print("Offer applied.")

# find(): Gets the position of a given word/char's first instance
feedback="The driver was polite and the ride was smooth."
word_to_search = "was"
print(f"Position of {word_to_search} is {feedback.find("was")}.")

# Get first letters of each words as list
# "".join(): join the elements with the given delemitter
name = "hello world"
initials = [word[0].upper() for word in name.split()] # default delimitter: " " - space
print(initials)
print("".join(initials))

sentence="Hi guys! shall we go for a break now!"
word_count=len(sentence.split())
print(word_count)


