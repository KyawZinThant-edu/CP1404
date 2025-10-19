CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania", "SA": "South Australia"}
print(CODE_TO_NAME)

for code, name in CODE_TO_NAME.items():
    print(f"{code:3} is {name}")

state_code = input("Enter short state: ")
while state_code != "":
    try:
        print(f"{state_code.upper()} is {CODE_TO_NAME[state_code.upper()]}")  # Second string method added here
    except KeyError:
        print("Invalid short state")
    state_code = input("Enter short state: ")
