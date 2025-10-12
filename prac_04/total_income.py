def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    number_of_months = int(input("How many months? "))

    for month in range(1, number_of_months + 1):
        income = float(input(f"Enter income for month {month}: "))
        incomes.append(income)

    print_report(incomes)


def print_report(incomes):
    """Print monthly income report with cumulative totals."""
    print("\nIncome Report")
    print("-------------")
    total = 0
    for month in range(len(incomes)):
        total += incomes[month]
        print(f"Month {month + 1:2} - Income: ${incomes[month]:10.2f} Total: ${total:10.2f}")



main()