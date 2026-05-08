x = 5
y = 0

try:
    result = x / y
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
finally: # This block will always be executed, regardless of whether an exception occurred or not.
    print("This block is always executed.")