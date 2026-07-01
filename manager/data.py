import json
import os
from models import Transaction, Expense, InventoryItem

FOLDER = "data"
EXPENSE_FILE = os.path.join(FOLDER, "expenses.json")
SALE_FILE = os.path.join(FOLDER, "sale.json")
INVENTORY_FILE = os.path.join(FOLDER, "inventory.json")

def ensure_folder():
    if not os.path.exists(FOLDER):
        os.makedirs(FOLDER)


def save_transaction(transaction):
    ensure_folder()
    data = []
    if os.path.isfile(SALE_FILE):
        with open(SALE_FILE, "r") as file:
            data = json.load(file)
            
    data.append(transaction.to_dict())
    
    with open(SALE_FILE, "w") as file:
        json.dump(data, file, indent=4)

def save_expense(expense):
    ensure_folder()
    data = []
    if os.path.isfile(EXPENSE_FILE):
        with open(EXPENSE_FILE, "r") as file:
            data = json.load(file)
            
    data.append(expense.to_dict())
    
    with open(EXPENSE_FILE, "w") as file:
        json.dump(data, file, indent=4)

def save_inventory_item(item):
    ensure_folder()
    data = []
    if os.path.isfile(INVENTORY_FILE):
        with open(INVENTORY_FILE, "r") as file:
            data = json.load(file)
            
    data.append(item.to_dict())
    
    with open(INVENTORY_FILE, "w") as file:
        json.dump(data, file, indent=4)


def load_all_transactions():
    transactions = []
    if not os.path.isfile(SALE_FILE):
        return transactions
        
    with open(SALE_FILE, "r") as file:
        data = json.load(file)
        for row in data:
            try:
                transactions.append(Transaction(
                    customer=row["customer"],
                    product=row["product"],
                    description=row["description"],
                    category=row["category"],
                    amount=row["amount"],
                    date=row.get("date"),
                    tx_id=row.get("id")
                ))
            except (ValueError, KeyError):
                continue
    return transactions

def load_all_expenses():
    expenses = []
    if not os.path.isfile(EXPENSE_FILE):
        return expenses
        
    with open(EXPENSE_FILE, "r") as file:
        data = json.load(file)
        for row in data:
            try:
                expenses.append(Expense(
                    name=row["name"],
                    description=row["description"],
                    category=row["category"],
                    amount=row["amount"],
                    date=row.get("date"),
                    tx_id=row.get("id")
                ))
            except (ValueError, KeyError):
                continue
    return expenses

def load_all_inventory():
    inventory = []
    if not os.path.isfile(INVENTORY_FILE):
        return inventory
        
    with open(INVENTORY_FILE, "r") as file:
        data = json.load(file)
        for row in data:
            try:
                inventory.append(InventoryItem(
                    name=row["name"],
                    description=row["description"],
                    category=row["category"],
                    quantity=row["quantity"],
                    item_id=row.get("id")
                ))
            except (ValueError, KeyError):
                continue
    return inventory


def rewrite_all_data(transactions):
    ensure_folder()
    from models import Transaction, Expense
    
    sales = [t.to_dict() for t in transactions if isinstance(t, Transaction)]
    expenses = [t.to_dict() for t in transactions if isinstance(t, Expense)]

    with open(SALE_FILE, "w") as f:
        json.dump(sales, f, indent=4)

    with open(EXPENSE_FILE, "w") as f:
        json.dump(expenses, f, indent=4)

def rewrite_all_inventory(inventory_list):
    ensure_folder()
    
    items = [item.to_dict() for item in inventory_list]
    
    with open(INVENTORY_FILE, "w") as f:
        json.dump(items, f, indent=4)