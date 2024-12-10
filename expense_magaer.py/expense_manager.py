import os
import json

class ExpenseManager:
    def __init__(self, file_name="expenses.json"):
        """Initializes the manager and loads expenses from a file."""
        self.file_name = file_name
        self.expenses = self._load_expenses()

    def _load_expenses(self):
        """Loads expenses from the file."""
        if os.path.exists(self.file_name):
            with open(self.file_name, 'r') as file:
                return json.load(file)
        return []

    def save_expenses(self):
        """Saves expenses to the file."""
        with open(self.file_name, 'w') as file:
            json.dump(self.expenses, file, indent=4)

    def add_expense(self, date, category, description, amount):
        """Adds a new expense to the list and saves it."""
        expense = {
            "date": date,
            "category": category,
            "description": description,
            "amount": float(amount)
        }
        self.expenses.append(expense)
        print(f"Added expense: {description} for ${amount} on {date} in category '{category}'.")
        self.save_expenses()

    def view_expenses(self):
        """Displays all expenses in a table-like format."""
        print("\nExpenses:")
        print(f"{'Date':<15} {'Category':<15} {'Description':<25} {'Amount':<10}")
        print("-" * 65)
        for expense in self.expenses:
            print(f"{expense['date']:<15} {expense['category']:<15} {expense['description']:<25} ${expense['amount']:<10.2f}")