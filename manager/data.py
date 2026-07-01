import csv
import os
from core import Transaction, Expense, InventoryItem

FOLDER = "data"
EXPENSE_FILE = os.path.join(FOLDER, "expenses.csv")
SALE_FILE = os.path.join(FOLDER, "sale.csv")
INVENTORY_FILE = os.path.join(FOLDER, "inventory.csv")

def ensure_folder():
    if not os.path.exists(FOLDER):
        os.makedirs(FOLDER)

def save_transaction(transaction):
    ensure_folder()
    file_exists = os.path.isfile(SALE_FILE)
    with open(SALE_FILE, mode="a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["ID","Date", "Customer", "Product", "Description", "Category", "Amount"])
        writer.writerow(transaction.to_list())

def save_expense(transaction):
    ensure_folder()
    file_exists = os.path.isfile(EXPENSE_FILE)
    with open(EXPENSE_FILE, mode="a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["ID", "Date", "Name",  "Description", "Category", "Amount"])
        writer.writerow(transaction.to_list())

def load_all_transactions():
    transactions = []
    if not os.path.isfile(SALE_FILE):
        return transactions
    with open(SALE_FILE, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            try:
                transactions.append(Transaction(
                    customer=row["Customer"],
                    product=row["Product"],
                    description=row["Description"],
                    category=row["Category"],
                    amount=row["Amount"],
                    date=row["Date"],
                    tx_id=row.get("ID")
                ))
            except (ValueError, KeyError):
                continue
    return transactions

def load_all_expenses():
    expenses = []
    if not os.path.isfile(EXPENSE_FILE):
        return expenses
    with open(EXPENSE_FILE, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            try:
                expenses.append(Expense(
                    name=row["Name"],
                    description=row["Description"],
                    category=row["Category"],
                    amount=row["Amount"],
                    date=row["Date"],
                    tx_id=row.get("ID")
                ))
            except (ValueError, KeyError):
                continue
    return expenses

def rewrite_all_data(transactions):
    from core import Transaction, Expense
    sales = [t for t in transactions if isinstance(t, Transaction)]
    expenses = [t for t in transactions if isinstance(t, Expense)]

    with open(SALE_FILE, mode="w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Date", "Customer", "Product", "Description", "Category", "Amount"])
        for t in sales: writer.writerow(t.to_list())

    with open(EXPENSE_FILE, mode="w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Date", "Name", "Description", "Category", "Amount"])
        for t in expenses: writer.writerow(t.to_list())

def save_inventory_item(item):
    ensure_folder()
    file_exists = os.path.isfile(INVENTORY_FILE)
    with open(INVENTORY_FILE, mode="a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["ID", "Name", "Description", "Category", "Quantity"])
        writer.writerow(item.to_list())

def load_all_inventory():
    inventory = []
    if not os.path.isfile(INVENTORY_FILE):
        return inventory
    with open(INVENTORY_FILE, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            try:
                inventory.append(InventoryItem(
                    name=row["Name"],
                    description=row["Description"],
                    category=row["Category"],
                    quantity=row["Quantity"],
                    item_id=row.get("ID")
                ))
            except (ValueError, KeyError):
                continue
    return inventory

def rewrite_all_inventory(inventory_list):
    ensure_folder()
    with open(INVENTORY_FILE, mode="w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Name", "Description", "Category", "Quantity"])
        for item in inventory_list:
            writer.writerow(item.to_list())
