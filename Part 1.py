## Author: Karlo Esguerra
## Date Created: 20 April 2024
## Date last changed: 26 April 2024
## This program tracks the budget for a small massage business, handling expenses and income.
## Input/Output: Users will input expense and income data, and the program will output current budget status.

## Constants for categories
EXPENSE_CATEGORIES = {1: "Rent", 2: "Salary", 3: "Supplies", 4: "Utility"}
INCOME_CATEGORIES = {1: "Service", 2: "Product Sales"}
INITIAL_VALUE = 0.0  # Define the initial value for the budget items

## Starting balances for categories
expenses = {category: INITIAL_VALUE for category in EXPENSE_CATEGORIES.values()}
incomes = {category: INITIAL_VALUE for category in INCOME_CATEGORIES.values()}

def print_menu():
    ## Prints the user menu options.
    print("\n--- Budget Tracker Menu ---")
    print("1. Add Expense")
    print("2. Add Income")
    print("3. View Budget")
    print("4. Exit")

def add_expense():
    ## Adds an expense entry under a predefined category.
    for number, category in EXPENSE_CATEGORIES.items():
        print(f"{number}. {category}")
    try:
        choice = int(input("Select the number of the expense category: "))
        if choice in EXPENSE_CATEGORIES:
            category = EXPENSE_CATEGORIES[choice]
            amount = float(input(f"Enter the amount for {category}: "))
            expenses[category] += amount
            print(f"Added expense of {amount} to {category}.")
        else:
            print("Invalid category selection.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def add_income():
    ## Adds an income entry under a predefined category.
    for number, category in INCOME_CATEGORIES.items():
        print(f"{number}. {category}")
    try:
        choice = int(input("Select the number of the income category: "))
        if choice in INCOME_CATEGORIES:
            category = INCOME_CATEGORIES[choice]
            amount = float(input(f"Enter the amount for {category}: "))
            incomes[category] += amount
            print(f"Added income of {amount} to {category}.")
        else:
            print("Invalid category selection.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def view_budget():
    ## Calculates and displays the budget overview based on current data.
    total_expenses = sum(expenses.values())
    total_incomes = sum(incomes.values())
    balance = total_incomes - total_expenses
    print("\n--- Budget Overview ---")
    print("Detailed Expenses:")
    for category, amount in expenses.items():
        print(f"{category}: {amount}")
    print("Detailed Income:")
    for category, amount in incomes.items():
        print(f"{category}: {amount}")
    print(f"Total Income: {total_incomes}")
    print(f"Total Expenses: {total_expenses}")
    print(f"Current Balance: {balance}")

def main():
    ## Main function to run the budget tracking program.
    while True:
        print_menu()
        choice = input("Choose an option: ")
        if choice == '1':
            add_expense()
        elif choice == '2':
            add_income()
        elif choice == '3':
            view_budget()
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice, please try again.")

## Starting point of the script
if __name__ == "__main__":
    main()
