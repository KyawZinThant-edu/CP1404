from datetime import date

CURRENT_YEAR = date.today().year  # don’t hard-code 2022

class Guitar:
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self, as_of_year: int = CURRENT_YEAR):
        return as_of_year - self.year

    def is_vintage(self):
        return self.get_age() >= 50
