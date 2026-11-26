import json
import os

FILE_NAME = "expenses.json"


# Load expenses from file
def load_expenses():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            return []
    return []


# Save expenses to file
def save_expenses(expenses):
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)


# Add new expense
def add_expense(expenses):
    name = input("Enter expense name: ")
    category = input("Enter category: ")

    try:
        amount = float(input("Enter amount: "))

        if amount <= 0:
            print("Amount must be greater than zero.")
            return

        expense = {
            "name": name,
            "category": category,
            "amount": amount
        }

        expenses.append(expense)
        save_expenses(expenses)

        print("Expense added successfully!")

    except ValueError:
        print("Please enter a valid amount.")


# View all expenses
def view_expenses(expenses):
    if not expenses:
        print("No expenses found.")
        return

    print("\n----- ALL EXPENSES -----")

    for index, expense in enumerate(expenses, start=1):
        print(
            index,
            expense["name"],
            expense["category"],
            expense["amount"]
        )


# Calculate total expenses
def total_expenses(expenses):
    total = 0

    for expense in expenses:
        total += expense["amount"]

    print("Total Expenses: Rs.", total)


# Search by category
def search_expenses(expenses):
    category = input("Enter category to search: ").lower()

    found = False

    for expense in expenses:
        if expense["category"].lower() == category:
            print(expense)
            found = True

    if not found:
        print("No expense found in this category.")


# Delete expense
def delete_expense(expenses):
    view_expenses(expenses)

    if not expenses:
        return

    try:
        number = int(input("Enter expense number to delete: "))

        if 1 <= number <= len(expenses):
            expenses.pop(number - 1)
            save_expenses(expenses)
            print("Expense deleted successfully!")
        else:
            print("Invalid expense number.")

    except ValueError:
        print("Please enter a valid number.")


# Main program
def main():

    expenses = load_expenses()

    while True:

        print("\n===== PERSONAL EXPENSE TRACKER =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expenses")
        print("4. Search Expense")
        print("5. Delete Expense")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense(expenses)

        elif choice == "2":
            view_expenses(expenses)

        elif choice == "3":
            total_expenses(expenses)

        elif choice == "4":
            search_expenses(expenses)

        elif choice == "5":
            delete_expense(expenses)

        elif choice == "6":
            print("Thank you for using Expense Tracker!")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()