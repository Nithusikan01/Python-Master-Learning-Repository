# While loop
i = 0
while i < 6:
    print(i)
    i += 1
    if i == 4:
        break   # Stops the loop when the condition meets
print("The loop is over")

# With the else statement we can run a block of code once when the condition no longer is true
i = 0
while i < 6:
    print(i)
    i += 1
    if i == 3:
        continue  # Skip the execution of code below that within the loop and goes to the next iteration
else:
    print("The loop is over")

# for loop
for i in range(10):
    print(i)

for i in range(2, 15):
    print(i)

for i in range(2, 15, 2):
    print(i)

lst = [1, 2, 3, 4, 5, 6, 10, 100, 1000]
for element in lst:
    print(element)

# The else keyword in a for loop specifies a block of code to be executed when the loop is finished
for i in range(2, 15, 2):
    print(i)
else:
    print("Finally loop is finished.")