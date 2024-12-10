from expense_manager import ExpenseManager

if __name__ == "__main__":
    manager = ExpenseManager()

    manager.add_expense("2024-12-01", "Food", "Groceries", 50.75)
    manager.add_expense("2024-12-02", "Transport", "Bus Ticket", 2.50)

    manager.view_expenses()