# Method 1: Using input() function
name = input("Enter your name: ")
print(f"Hello, {name}!")

# Method 2: Using command-line arguments
import sys
args = sys.argv[1:]
print("Command-line arguments:", args)