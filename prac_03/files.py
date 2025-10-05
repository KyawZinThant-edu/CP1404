
# 1. Write name to file
name = input("Enter your name: ")
name_file = open("name.txt", "w")
name_file.write(name)
name_file.close()
print(f"Name '{name}' written to name.txt\n")

# 2. Read name from file and greet
name_file = open("name.txt", "r")
read_name = name_file.read().strip()
name_file.close()
print(f"Hi {read_name}!\n")

# 3. Read first two numbers and add them
with open("numbers.txt", "r") as numbers_file:
    first_number = int(numbers_file.readline().strip())
    second_number = int(numbers_file.readline().strip())
    total = first_number + second_number
    print(f"The sum of the first two numbers is: {total}\n")

# 4. Read all numbers and calculate total
total_all = 0
with open("numbers.txt", "r") as numbers_file:
    for line in numbers_file:
        number = int(line.strip())
        total_all += number
print(f"The total of all numbers is: {total_all}")