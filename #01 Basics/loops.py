# Example using different types of loops in Python

# For loop with a list
fruits = ["apple", "banana", "cherry"]
print("Using for loop with a list:")
for fruit in fruits:
    print(fruit)

# For loop with a range
print("\nUsing for loop with a range:")
for i in range(1, 5):
    print(i)

# While loop
print("\nUsing while loop:")
count = 0
while count < 5:
    print(count)
    count += 1

# For loop with break statement
print("\nUsing for loop with break statement:")
for i in range(10):
    if i == 5:
        break
    print(i)

# For loop with continue statement
print("\nUsing for loop with continue statement:")
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

# For loop with else statement
print("\nUsing for loop with else statement:")
for i in range(5):
    print(i)
else:
    print("Loop finished")

# Nested loops
print("\nUsing nested loops:")
for i in range(3):
    for j in range(2):
        print(i, j)