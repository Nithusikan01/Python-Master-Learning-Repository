"""
From a function's perspective:
    - A parameter is the variable listed inside the parentheses in the function definition.
    - An argument is the value that is sent to the function when it is called.
"""
def my_function():
    pass

def my_function_1():
    print("Hello world")

def my_function_2(word):
    return word + word

def my_function_3(arg1, arg2, arg3):
    print(arg1)
    print(arg2)
    return arg3 * arg2

# If the number of arguments is unknown, add a * before the parameter name:
def my_function_4(*args):
    for arg in args:
        print(arg)

# Keyword arguments: key: value pairs
def my_function_5(child_1='Kamal', child_2='vimal', child_3='vinoth'):
    print(child_1)
    print(child_2)
    print(child_3)

# If the number of keyword arguments is unknown, add a double ** before the parameter name:
def my_function_6(**kwargs):
      print("His last name is " + kwargs["lname"])

# Combine positional args only then keyword args together
def my_function_7(a, b, /, *, c, d):
  print(a + b + c + d)



def run():
    my_function_1()
    a = my_function_2("Hii")
    print(a)
    b = my_function_3(2, 3, 4)
    print(b)
    my_function_4(4,5,6,7,"hello", 7.8, 3.14)
    my_function_5(child_1="Ajith", child_2="Vijay", child_3="Surja")
    my_function_6(fname = "Tobias", lname = "Refsnes")
    my_function_7(5, 6, c = 7, d = 8)


if __name__ == "__main__":
    run()