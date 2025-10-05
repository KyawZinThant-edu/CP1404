import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

# What did you see on line 1?
# Answer: I saw numbers like 7, 15, 19, etc.

# What was the smallest number you could have seen, what was the largest?
# Smallest: 5, Largest: 20

# What did you see on line 2?
# Answer: I saw numbers like 3, 5, 7, 9

# What was the smallest number you could have seen, what was the largest?
# Smallest: 3, Largest: 9

# Could line 2 have produced a 4?
# Answer: No, because randrange(3, 10, 2) generates numbers in steps of 2: 3, 5, 7, 9

# What did you see on line 3?
# Answer: I saw numbers like 3.156, 4.892, 2.734, etc.

# What was the smallest number you could have seen, what was the largest?
# Smallest: 2.5, Largest: 5.5

random_number = random.randint(1,100)
print(f"random number between 1 and 100: {random_number}")