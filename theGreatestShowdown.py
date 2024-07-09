#Task 1: Identify the Greatest:
# Ask the user to enter three numbers.
number1 = float(input("enter the first number"))
number2 = float(input("enter the secont number"))
number3 = float(input("enter the third number"))
## Determine the largest number.
if number1 >= number2 and number1 >= number3:
  largest = number1
elif number2 >=number1 and number2 >= number3:
  largest = number2
else:
  largest = number3

#Task 2: Identify the Smallest:
## Determine the Smallest number.
if number1 <= number2 and number1 <= number3:
  smallest = number1
elif number2 <=number1 and number2 <= number3:
  smallest = number2
else:
  smallest = number3

#Print the largest and smallest numbers.
print("the largest number among the three is:", largest)
print("he smallest number among the three is:", smallest)