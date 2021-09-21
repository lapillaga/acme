import sys

from acme.helpers.file import read_lines_from_file
from acme.helpers.helpers import get_employee_data


def display_menu():
    print("""
        ACME Menu
        1. Calculate from demo.txt file
        2. Calculate from input
        3. Quit acme
    """)


class App:
    """Acme app main class."""
    def __init__(self):
        self.choices = {
            "1": self.calculate_from_file,
            "2": self.calculate_from_input,
            "3": self.quit
        }

    def run(self):
        while True:
            display_menu()
            choice = input("Please enter an option: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("{0} is not a valid choice".format(choice))

    def calculate_from_file(self):
        lines = read_lines_from_file('demo.txt')

        for line in lines:
            employee_name, work_days = get_employee_data(line)
            print(employee_name)
            print(work_days)
        print(lines)

    def calculate_from_input(self):
        pass

    def quit(self):
        """Terminate program"""
        print("Thanks for use ACME")
        sys.exit(0)