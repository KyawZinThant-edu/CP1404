# Basic list operations
def basic_list_operations():
    """Get 5 numbers from user and display information about them."""
    numbers = []

    for i in range(5):
        number = float(input("Number: "))
        numbers.append(number)

    print(f"The first number is {numbers[0]}")
    print(f"The last number is {numbers[-1]}")
    print(f"The smallest number is {min(numbers)}")
    print(f"The largest number is {max(numbers)}")
    print(f"The average of the numbers is {sum(numbers) / len(numbers)}")


# Security checker
def security_checker():
    """Check if username is in authorized list."""
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45',
                 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState',
                 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

    username = input("Enter your username: ")

    if username in usernames:
        print("Access granted")
    else:
        print("Access denied")


# Main program to run both exercises
def main():
    print("=== Basic List Operations ===")
    basic_list_operations()

    print("\n=== Security Checker ===")
    security_checker()


main()