# Task 1: Code Correction:
number = float(input("Enter a number: "))
# Converted the input to an float.
if number > 0:
    print("The number is positive.")
elif number == 0:
# Changed the single = to == equality comparison operator.
    print("The number is zero.")
else:
# Removed the condition in the else statement.
    print("The number is negative.")