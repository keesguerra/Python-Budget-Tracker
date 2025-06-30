## Author: Karlo Esguerra
## Date Created: 20 April 2024
## Date last changed: 26 April 2024
## This program tracks the budget for a small massage business, handling expenses and income.
## Input/Output: Users will input expense and income data, and the program will output current budget status.

import tkinter as tk
from tkinter import messagebox, ttk
import os

## Set theme for better styling
style = ttk.Style()
style.theme_use('clam')

## Constants for predefined categories
EXPENSE_CATEGORIES = ["Rent", "Salary", "Supplies", "Utility"]
INCOME_CATEGORIES = ["Service", "Product Sales"]

## Starting balances for categories
expenses = {category: 0.0 for category in EXPENSE_CATEGORIES}
incomes = {category: 0.0 for category in INCOME_CATEGORIES}

## Function to read external file
def read_file(filename):
    if not os.path.isfile(filename):
        print(f"No file found at {filename}, starting with an empty budget.")
        return
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            category_type = parts[0].strip().lower()
            category = parts[1].strip()
            amount = float(parts[2].strip())
            if category_type == 'expense' and category in expenses:
                expenses[category] += amount
            elif category_type == 'income' and category in incomes:
                incomes[category] += amount
    update_budget_overview()

## Function to update the budget overview
def update_budget_overview():
    total_expenses = sum(expenses.values())
    total_incomes = sum(incomes.values())
    balance = total_incomes - total_expenses
    budget_overview_label.config(text=f"Total Income: {total_incomes}\nTotal Expenses: {total_expenses}\nCurrent Balance: {balance}")

## Function to add an expense
def add_expense():
    category = expense_category.get()
    amount = expense_amount_entry.get()
    if amount:
        expenses[category] += float(amount)
        update_budget_overview()
    expense_amount_entry.delete(0, tk.END)

## Function to add an income
def add_income():
    category = income_category.get()
    amount = income_amount_entry.get()
    if amount:
        incomes[category] += float(amount)
        update_budget_overview()
    income_amount_entry.delete(0, tk.END)
   
## Function to ask before exiting
def exit_application():
    if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
        root.destroy()

## Set up the main GUI window
root = tk.Tk()
root.title("Budget Tracker for Small Massage Business")
root.configure(bg='white')  # White background for the GUI

## Define the layout with grid
## Labels
ttk.Label(root, text="Expense Category").grid(row=0, column=0, padx=10, pady=10, sticky="W")
ttk.Label(root, text="Income Category").grid(row=2, column=0, padx=10, pady=10, sticky="W")

## Dropdown menus for categories
expense_category = ttk.Combobox(root, values=EXPENSE_CATEGORIES, width=18)
expense_category.grid(row=0, column=1, padx=10, pady=10)
expense_category.set(EXPENSE_CATEGORIES[0])

income_category = ttk.Combobox(root, values=INCOME_CATEGORIES, width=18)
income_category.grid(row=2, column=1, padx=10, pady=10)
income_category.set(INCOME_CATEGORIES[0])

## Entry fields for amounts
expense_amount_entry = ttk.Entry(root, width=21)
expense_amount_entry.grid(row=1, column=1, padx=10, pady=10)

income_amount_entry = ttk.Entry(root, width=21)
income_amount_entry.grid(row=3, column=1, padx=10, pady=10)

## Buttons for adding expenses and income with subtle styling
add_expense_button = ttk.Button(root, text="Add Expense", command=add_expense)
add_expense_button.grid(row=1, column=2, padx=10, pady=10)

add_income_button = ttk.Button(root, text="Add Income", command=add_income)
add_income_button.grid(row=3, column=2, padx=10, pady=10)

## Label to display the budget overview
budget_overview_label = ttk.Label(root, text="Budget Overview will be shown here", justify=tk.LEFT)
budget_overview_label.grid(row=4, column=0, columnspan=3, padx=10, pady=20)

## Exit button 
exit_button = ttk.Button(root, text="Exit", command=exit_application)
exit_button.grid(row=5, column=1, padx=10, pady=10, sticky='E')

## Initial budget overview update
update_budget_overview()

## Start the script by reading the budget data from a file
if __name__ == "__main__":
    read_file('budget_data.txt')
    root.mainloop()
