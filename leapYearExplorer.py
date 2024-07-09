#Task 1: Leap Year Checker
year = int(input("enter a year "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
  print(year, "is a leap year ")
else:
  print("is not a leap year")