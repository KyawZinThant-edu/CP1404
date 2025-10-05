"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
"""

is_finished = False
while not is_finished:
    try:
        result = int(input("Enter a valid integer: "))
        is_finished = True  # This line will only run if no exception occurs
    except ValueError:  # This will catch when the input cannot be converted to an integer
        print("Please enter a valid integer.")

print("Valid result is:", result)