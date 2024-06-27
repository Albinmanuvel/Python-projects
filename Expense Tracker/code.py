import csv
from datetime import datetime

class ExpenseTracker:
    def __init__(self, filename='expenses.csv'):
        self.filename = filename
        self.expenses = []
        self.load_expenses()

    def load_expenses(self):
        try:
            with open(self.filename, 'r') as file:
                reader = csv.DictReader(file)
                self.expenses = list(reader)
        except FileNotFoundError:
            self.expenses = []

    def save_expenses(self):
        with open(self.filename, 'w', newline='') as file:
            fieldnames = ['date', 'category', 'amount', 'description']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(self.expenses)

    def add_expense(self, category, amount, description):
        date = datetime.now().strftime('%Y-%m-%d')
        expense = {
            'date': date,
            'category': category,
            'amount': amount,
            'description': description
        }
        self.expenses.append(expense)
        self.save_expenses()

    def view_expenses(self):
        if not self.expenses:
            print("No expenses recorded.")
            return
        for expense in self.expenses:
            print(f"{expense['date']} | {expense['category']} | ${expense['amount']} | {expense['description']}")

    def view_summary(self):
        if not self.expenses:
            print("No expenses recorded.")
            return
        total = sum(float(expense['amount']) for expense in self.expenses)
        print(f"Total expenses: ${total:.2f}")

        categories = {}
        for expense in self.expenses:
            category = expense['category']
            amount = float(expense['amount'])
            if category in categories:
                categories[category] += amount
            else:
                categories[category] = amount

        print("\nExpenses by category:")
        for category, amount in categories.items():
            print(f"{category}: ${amount:.2f}")

def main():
    tracker = ExpenseTracker()

    while True:
        print("\n--- Expense Tracker ---")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Summary")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            category = input("Enter expense category: ")
            amount = input("Enter expense amount: ")
            description = input("Enter expense description: ")
            tracker.add_expense(category, amount, description)
            print("Expense added successfully!")

        elif choice == '2':
            tracker.view_expenses()

        elif choice == '3':
            tracker.view_summary()

        elif choice == '4':
            print("Thank you for using Expense Tracker. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()