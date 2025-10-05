"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

while True:
    try:
        numerator = int(input("Enter the numerator: "))
        break
    except ValueError:
        print("Please enter a valid integer for numerator!")

while True:
    try:
        denominator = int(input("Enter the denominator: "))
        if denominator == 0:
            print("Denominator cannot be zero! Please try again.")
            continue
        break
    except ValueError:
        print("Please enter a valid integer for denominator!")

fraction = numerator / denominator
print(f"{numerator} / {denominator} = {fraction}")
print("Program finished.")



# 1. When will a ValueError occur?
#    A ValueError will occur when the user enters something that cannot be converted to an integer,
#    such as letters, symbols, or decimal numbers (if using int()).

# 2. When will a ZeroDivisionError occur?
#    A ZeroDivisionError will occur when the user enters 0 for the denominator.

# 3. Could you change the code to avoid the possibility of a ZeroDivisionError?
#    Yes, by adding a check to ensure the denominator is not zero before performing the division.