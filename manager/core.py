import datetime

class Transaction:
    def __init__(self, customer, product, description, category, amount,  date=None, tx_id=None):
        self.customer = customer.strip()
        self.product = product.strip()
        self.description = description.strip()
        self.category = category.strip().capitalize()
        self.amount = self._validate_amount(amount)
        self.date = date if date else datetime.date.today().strftime("%Y-%m-%d")
        self.id = int(tx_id) if tx_id is not None else None

    def _validate_amount(self, value):
        try:
            val = float(value)
            if val <= 0:
                raise ValueError("Amount must be positive")
            return round(val, 2)
        except (ValueError, TypeError):
            raise ValueError("Invalid number format")

    def to_list(self):
        return [self.id, self.date, self.customer, self.product, self.description, self.category, self.amount]

class Expense:
    def __init__(self, name, description, category, amount,  date=None, tx_id=None):
        self.name = name.strip()
        self.description = description.strip()
        self.category = category.strip().capitalize()
        self.amount = self._validate_amount(amount)
        self.date = date if date else datetime.date.today().strftime("%Y-%m-%d")
        self.id = int(tx_id) if tx_id is not None else None

    def _validate_amount(self, value):
        try:
            val = float(value)
            if val <= 0:
                raise ValueError("Amount must be positive")
            return round(val, 2)
        except (ValueError, TypeError):
            raise ValueError("Invalid number format")

    def to_list(self):
        return [self.id, self.date, self.name, self.description, self.category, self.amount]

class InventoryItem:
        def __init__(self, name, description, category, quantity, item_id=None):
            self.name = name.strip()
            self.description = description.strip()
            self.category = category.strip().capitalize()
            try:
                self.quantity = int(quantity)
            except ValueError:
                raise ValueError("Quantity must be a whole number")

            self.id = int(item_id) if item_id is not None else None

        def to_list(self):
            return [self.id, self.name, self.description, self.category, self.quantity]

class BusinessManager:
    def __init__(self):
        self.transactions = []
        self.inventory = []

    def add_transaction(self, obj):
        from core import Transaction, Expense
        if isinstance(obj, Transaction):
            if obj.id is None:
                obj.id = self.get_next_sale_id()
            self.transactions.append(obj)
        elif isinstance(obj, Expense):
            if obj.id is None:
                obj.id = self.get_next_expense_id()
            self.transactions.append(obj)

    def get_next_sale_id(self):
            from core import Transaction
            sales_ids = [t.id for t in self.transactions if isinstance(t, Transaction) and t.id is not None]
            return max(sales_ids) + 1 if sales_ids else 1

    def get_next_expense_id(self):
        from core import Expense
        expense_ids = [t.id for t in self.transactions if isinstance(t, Expense) and t.id is not None]
        return max(expense_ids) + 1 if expense_ids else 1

    def add_inventory_item(self, item_obj):
        if isinstance(item_obj, InventoryItem):
            if item_obj.id is None:
                item_obj.id = self.get_next_inv_id()
            self.inventory.append(item_obj)

    def get_next_inv_id(self):
        if not self.inventory:
            return 1
        existing_ids = [item.id for item in self.inventory if item.id is not None]
        return max(existing_ids) + 1 if existing_ids else 1

    def get_totals(self):
        sales = sum(t.amount for t in self.transactions if t.category == "Sale")
        expenses = sum(t.amount for t in self.transactions if t.category == "Expense")
        return {"sales": sales, "expenses": expenses, "net": sales - expenses}



def format_currency(value):
    return f"${value:,.2f}"
