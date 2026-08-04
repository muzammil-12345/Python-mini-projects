# Day 12: Expense Tracker project

# Step 1: Initialize an empty list to store expenses

expenses = []

# Step 2: Display the menu
def show_menu():
    print("\n--- Expense Tracker Menu ---")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Search Expense")
    print("4. Edit Expense")
    print("5. Delete Expense")
    print("6. Exit")

# Step 3: Add an Expense
def add_expense():
    item = input("Expense item: ")
    Category = input("Category (Food/Travel/Bills/Others): ")
    amount = float(input("Amount: "))
    expenses.append({"item": item, "category": Category, "amount": amount})
    print(f"Expense '{item}' has been added successfully!")

# Step 4: View All Expenses
def view_expenses():
    if expenses:
        print("\n--- Expense List ---")
        for expense in expenses:
            print(f"Item: {expense['item']}, Category: {expense['category']}, Amount: {expense['amount']}")
    else:
        print("No expenses recorded.")

# for total expense
def total_expense():
    total = sum(exp["amount"] for exp in expenses)
    print(f"Total Expense: {total}")

# Step 5: Category wise summary
def category_summary():
    summary = {}
    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]
        if category in summary:
            summary[category] += amount
        else:
            summary[category] = amount
    print("\n--- Category-wise Summary ---")
    for category, total in summary.items():
        print(f"{category}: {total}")

# Search an Expense
def search_expense():
    query = input("Enter expense item to search: ").strip().lower()
    matches = [expense for expense in expenses if query in expense["item"].lower()]
    if matches:
        print("\n--- Search Results ---")
        for expense in matches:
            print(f"Item: {expense['item']}, Category: {expense['category']}, Amount: {expense['amount']}")
    else:
        print("No matching expenses found.")

# Edit an Expense
def edit_expense():
    item_to_edit = input("Enter expense item to edit: ").strip().lower()
    for expense in expenses:
        if expense["item"].lower() == item_to_edit:
            new_item = input(f"New item name (leave blank to keep '{expense['item']}'): ").strip()
            new_category = input(f"New category (leave blank to keep '{expense['category']}'): ").strip()
            new_amount = input(f"New amount (leave blank to keep '{expense['amount']}'): ").strip()
            if new_item:
                expense["item"] = new_item
            if new_category:
                expense["category"] = new_category
            if new_amount:
                try:
                    expense["amount"] = float(new_amount)
                except ValueError:
                    print("Invalid amount entered. Keeping the previous amount.")
            print("Expense updated successfully.")
            return
    print("Expense not found.")

# Delete an Expense
def delete_expense():
    item_to_delete = input("Enter expense item to delete: ").strip().lower()
    for index, expense in enumerate(expenses):
        if expense["item"].lower() == item_to_delete:
            del expenses[index]
            print("Expense deleted successfully.")
            return
    print("Expense not found.")

# Step 6: Saving into a file
def save_expenses_to_file():
    with open("expenses.txt", "w") as file:
        for expense in expenses:
            file.write(f"{expense['item']},{expense['category']},{expense['amount']}\n")
    print("Expenses saved to 'expenses.txt'.")

# Step 7: Main loop to run the app
def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-6): ")
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
            total_expense()
            category_summary()
        elif choice == "3":
            search_expense()
        elif choice == "4":
            edit_expense()
        elif choice == "5":
            delete_expense()
        elif choice == "6":
            save_expenses_to_file()
            print("Exiting the app. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")    


main()            
