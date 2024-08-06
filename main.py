import csv
import datetime

# Constants
EXPENSES_FILE = 'expenses.csv'

def initialize_csv():
    try:
        with open(EXPENSES_FILE, mode='x', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Date', 'Description', 'Category', 'Amount'])
    except FileExistsError:
        pass

def add_expense(date, description, category, amount):
    """Add a new expense entry."""
    with open(EXPENSES_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, description, category, amount])
    print("Expense added successfully!")

def view_expenses():
    """View all expenses."""
    with open(EXPENSES_FILE, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        print("Date\tDescription\tCategory\tAmount")
        for row in reader:
            print('\t'.join(row))

def edit_expense(row_num, date, description, category, amount):
    """Edit an existing expense entry."""
    rows = []
    with open(EXPENSES_FILE, mode='r') as file:
        reader = csv.reader(file)
        rows = list(reader)
    
    if row_num < 1 or row_num >= len(rows):
        print("Invalid row number.")
        return

    rows[row_num] = [date, description, category, amount]
    
    with open(EXPENSES_FILE, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)
    print("Expense updated successfully!")

def delete_expense(row_num):
    """Delete an expense entry."""
    rows = []
    with open(EXPENSES_FILE, mode='r') as file:
        reader = csv.reader(file)
        rows = list(reader)
    
    if row_num < 1 or row_num >= len(rows):
        print("Invalid row number.")
        return

    rows.pop(row_num)
    
    with open(EXPENSES_FILE, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)
    print("Expense deleted successfully!")

def generate_summary():
    """Generate a summary report of expenses."""
    summary = {}
    with open(EXPENSES_FILE, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            category, amount = row[2], float(row[3])
            if category in summary:
                summary[category] += amount
            else:
                summary[category] = amount

    print("Category\tTotal Amount")
    for category, total in summary.items():
        print(f"{category}\t{total:.2f}")

def main():
    initialize_csv()
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Edit Expense")
        print("4. Delete Expense")
        print("5. Generate Summary")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            date = input("Enter date (YYYY-MM-DD): ")
            description = input("Enter description: ")
            category = input("Enter category: ")
            amount = float(input("Enter amount: "))
            add_expense(date, description, category, amount)
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            row_num = int(input("Enter the row number to edit: "))
            date = input("Enter new date (YYYY-MM-DD): ")
            description = input("Enter new description: ")
            category = input("Enter new category: ")
            amount = float(input("Enter new amount: "))
            edit_expense(row_num, date, description, category, amount)
        elif choice == '4':
            row_num = int(input("Enter the row number to delete: "))
            delete_expense(row_num)
        elif choice == '5':
            generate_summary()
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
