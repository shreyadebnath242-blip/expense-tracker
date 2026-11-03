"""Simple command-line expense tracker.
Saves expenses to expenses.json so data stays after you close the program.
"""
import json
import os

FILE_NAME = "expenses.json"


def load_expenses():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    return []


def save_expenses(expenses):
    with open(FILE_NAME, "w") as f:
        json.dump(expenses, f, indent=2)


def add_expense(expenses):
    name = input("What did you spend on? ")
    category = input("Category (food/travel/study/other): ").lower()
    try:
        amount = float(input("Amount in Rs: "))
    except ValueError:
        print("Please enter a valid number.")
        return
    expenses.append({"name": name, "category": category, "amount": amount})
    save_expenses(expenses)
    print("Expense added!")


def view_expenses(expenses):
    if not expenses:
        print("No expenses yet.")
        return
    for i, e in enumerate(expenses, start=1):
        print(f"{i}. {e['name']} ({e['category']}) - Rs {e['amount']:.2f}")


def summary(expenses):
    totals = {}
    for e in expenses:
        totals[e["category"]] = totals.get(e["category"], 0) + e["amount"]
    for category, total in sorted(totals.items(), key=lambda x: x[1], reverse=True):
        print(f"{category}: Rs {total:.2f}")
    print(f"TOTAL: Rs {sum(totals.values()):.2f}")


def main():
    expenses = load_expenses()
    while True:
        print("\n1. Add expense  2. View expenses  3. Summary  4. Quit")
        choice = input("Choose: ")
        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            summary(expenses)
        elif choice == "4":
            print("Bye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
