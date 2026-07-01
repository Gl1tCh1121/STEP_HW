import pytest
from core import Transaction, Expense, InventoryItem, BusinessManager

# --- 1. DATA VALIDATION TESTS ---

def test_transaction_init_cleaning():
    """Test if Transaction class cleans whitespace and handles numbers."""
    t = Transaction("  John Doe  ", " Laptop ", " Work tool ", "Sale", " 1500.50 ")
    assert t.customer == "John Doe"
    assert t.product == "Laptop"
    assert t.amount == 1500.50
    assert t.category == "Sale"

def test_expense_init_cleaning():
    """Test if Expense class cleans whitespace and handles numbers."""
    e = Expense("  Electricity  ", " Bill for March ", "Expense", " 200 ")
    assert e.name == "Electricity"
    assert e.amount == 200.0
    assert e.category == "Expense"

def test_inventory_init_cleaning():
    """Test if InventoryItem ensures quantity is an integer."""
    i = InventoryItem("  Hammer  ", " Steel ", " Tools ", " 15 ")
    assert i.name == "Hammer"
    assert i.quantity == 15
    assert isinstance(i.quantity, int)

def test_invalid_formats():
    """Ensure the classes raise ValueError for bad number inputs."""
    with pytest.raises(ValueError):
        Transaction("C", "P", "D", "Sale", "abc")
    with pytest.raises(ValueError):
        Expense("N", "D", "Expense", "-50")
    with pytest.raises(ValueError):
        InventoryItem("N", "D", "C", "10.5")

# --- 2. ID LOGIC TESTS (CRITICAL) ---

def test_id_isolation():
    """Verify that Sales, Expenses, and Inventory count IDs independently."""
    mgr = BusinessManager()

    s1 = Transaction("C1", "P1", "D", "Sale", "100")
    e1 = Expense("E1", "D", "Expense", "50")
    i1 = InventoryItem("I1", "D", "C", "10")

    mgr.add_transaction(s1)
    mgr.add_transaction(e1)
    mgr.add_inventory_item(i1)

    # All should start at ID 1
    assert s1.id == 1
    assert e1.id == 1
    assert i1.id == 1

    # Add a second Sale - should be ID 2
    s2 = Transaction("C2", "P2", "D", "Sale", "200")
    mgr.add_transaction(s2)
    assert s2.id == 2
    # Verify expense ID stayed at 1
    assert e1.id == 1

# --- 3. BUSINESS LOGIC & MATH TESTS ---

def test_manager_totals_calculation():
    """Test if the manager calculates Sales, Expenses, and Net correctly."""
    mgr = BusinessManager()
    mgr.add_transaction(Transaction("C1", "P1", "D", "Sale", "1000"))
    mgr.add_transaction(Transaction("C2", "P2", "D", "Sale", "500"))
    mgr.add_transaction(Expense("E1", "D", "Expense", "300"))

    totals = mgr.get_totals()
    assert totals["sales"] == 1500.0
    assert totals["expenses"] == 300.0
    assert totals["net"] == 1200.0

def test_empty_manager():
    """Ensure manager doesn't crash if no data is present."""
    mgr = BusinessManager()
    totals = mgr.get_totals()
    assert totals["sales"] == 0
    assert totals["expenses"] == 0
    assert totals["net"] == 0

# --- 4. EDITOR LOGIC (IN-MEMORY UPDATE) ---

def test_edit_update_logic():
    """Simulate the Editor updating an existing record in memory."""
    mgr = BusinessManager()
    t = Transaction("Old Name", "Old Product", "Desc", "Sale", "100")
    mgr.add_transaction(t)

    # Find the object by ID and change it
    target = next(item for item in mgr.transactions if item.id == 1)
    target.customer = "New Name"
    target.amount = 200.0

    # Verify the object in the list is updated
    assert mgr.transactions[0].customer == "New Name"
    assert mgr.transactions[0].amount == 200.0
