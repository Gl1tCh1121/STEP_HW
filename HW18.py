import os
from datetime import datetime
import pandas as pd

CSV_FILE = "products.csv"
LOG_FILE = "log.txt"

def log_action(user, action, details=""):
    """ინახავს თითოეულ მოქმედებას log.txt ფაილში"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_msg = f"[{timestamp}] USER={user} | ACTION={action}"
    if details:
        log_msg += f" | {details}"
    
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(log_msg + "\n")

def initialize_csv():
    """ქმნის საწყის CSV ფაილს pandas-ის საშუალებით, თუ ის არ არსებობს"""
    if not os.path.exists(CSV_FILE):
        df = pd.DataFrame([
            {"id": "1", "name": "Apple", "price": "2.5", "stock": "100"},
            {"id": "2", "name": "Banana", "price": "1.2", "stock": "150"},
            {"id": "3", "name": "Milk", "price": "4.0", "stock": "50"}
        ])
        df.to_csv(CSV_FILE, index=False)

# 1. ყველა პროდუქტის ნახვა
def show_all_products(user):
    df = pd.read_csv(CSV_FILE, dtype=str)
    log_action(user, "VIEW_ALL_PRODUCTS")
    
    if df.empty:
        print("\n❌ No products found.")
        return
        
    print("\n--- Products List ---")
    for _, row in df.iterrows():
        print(f"ID: {row['id']} | Name: {row['name']} | Price: ${row['price']} | Stock: {row['stock']}")

# 2. პროდუქტის მოძებნა ID-ით
def get_product_by_id(user):
    prod_id = input("Enter product ID to search: ").strip()
    df = pd.read_csv(CSV_FILE, dtype=str)
    log_action(user, "GET_PRODUCT", f"PRODUCT_ID={prod_id}")
    
    product = df[df['id'] == prod_id]
    if not product.empty:
        p = product.iloc[0]
        print(f"\n✅ Found: ID: {p['id']} | Name: {p['name']} | Price: ${p['price']} | Stock: {p['stock']}")
    else:
        print("\n❌ Product not found.")

# 3. პროდუქტის დამატება
def add_product(user):
    name = input("Enter product name: ").strip()
    price = input("Enter product price: ").strip()
    stock = input("Enter product stock: ").strip()
    
    df = pd.read_csv(CSV_FILE, dtype=str)
    
    # ავტომატური ID-ის გენერაცია მაქსიმალურ ID + 1 პრინციპით
    if not df.empty:
        next_id = str(df['id'].astype(int).max() + 1)
    else:
        next_id = "1"
        
    new_product = pd.DataFrame([{"id": next_id, "name": name, "price": price, "stock": stock}])
    df = pd.concat([df, new_product], ignore_index=True)
    df.to_csv(CSV_FILE, index=False)
    
    log_action(user, "ADD_PRODUCT", f"NAME={name}")
    print(f"\n✅ Product added successfully with ID: {next_id}")

# 4. პროდუქტის წაშლა
def delete_product(user):
    prod_id = input("Enter product ID to delete: ").strip()
    df = pd.read_csv(CSV_FILE, dtype=str)
    
    if prod_id in df['id'].values:
        df = df[df['id'] != prod_id]
        df.to_csv(CSV_FILE, index=False)
        log_action(user, "DELETE_PRODUCT", f"PRODUCT_ID={prod_id}")
        print("\n✅ Product deleted successfully.")
    else:
        log_action(user, "DELETE_PRODUCT", f"PRODUCT_ID={prod_id} (FAILED - NOT FOUND)")
        print("\n❌ Product not found.")

# მთავარი მენიუ
def main():
    initialize_csv()
    print("=== Product Management System ===")
    user = input("Enter your name: ").strip()
    if not user:
        user = "Unknown_User"

    while True:
        print("\nMenu:")
        print("1. Show all products")
        print("2. Get product by id")
        print("3. Add product")
        print("4. Delete product")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ").strip()
        
        if choice == "1":
            show_all_products(user)
        elif choice == "2":
            get_product_by_id(user)
        elif choice == "3":
            add_product(user)
        elif choice == "4":
            delete_product(user)
        elif choice == "5":
            print(f"\nGoodbye, {user}!")
            break
        else:
            print("\n❌ Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()