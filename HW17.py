import csv
import os
from datetime import datetime

CSV_FILE = "products.csv"
LOG_FILE = "log.txt"

# ლოგირების ფუნქცია
def log_action(user, action, details=""):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_msg = f"[{timestamp}] USER={user} | ACTION={action}"
    if details:
        log_msg += f" | {details}"
    
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(log_msg + "\n")

# CSV ფაილის ინიციალიზაცია (თუ არ არსებობს)
if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["id", "name", "price", "stock"])
        # სატესტო მონაცემები
        writer.writerows([
            ["1", "Apple", "2.5", "100"],
            ["2", "Banana", "1.2", "150"],
            ["3", "Milk", "4.0", "50"]
        ])

# პროდუქტების წაკითხვა ფაილიდან
def read_products():
    products = []
    with open(CSV_FILE, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            products.append(row)
    return products

# პროდუქტების ჩაწერა ფაილში
def write_products(products):
    with open(CSV_FILE, "w", newline="", encoding="utf-8") as f:
        fieldnames = ["id", "name", "price", "stock"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(products)

# 1. ყველა პროდუქტის ნახვა
def show_all_products(user):
    products = read_products()
    log_action(user, "VIEW_ALL_PRODUCTS")
    
    if not products:
        print("\n❌ No products found.")
        return
        
    print("\n--- Products List ---")
    for p in products:
        print(f"ID: {p['id']} | Name: {p['name']} | Price: ${p['price']} | Stock: {p['stock']}")

# 2. პროდუქტის მოძებნა ID-ით
def get_product_by_id(user):
    prod_id = input("Enter product ID to search: ").strip()
    products = read_products()
    log_action(user, "GET_PRODUCT", f"PRODUCT_ID={prod_id}")
    
    for p in products:
        if p['id'] == prod_id:
            print(f"\n✅ Found: ID: {p['id']} | Name: {p['name']} | Price: ${p['price']} | Stock: {p['stock']}")
            return
    print("\n❌ Product not found.")

# 3. პროდუქტის დამატება
def add_product(user):
    name = input("Enter product name: ").strip()
    price = input("Enter product price: ").strip()
    stock = input("Enter product stock: ").strip()
    
    products = read_products()
    
    # ახალი უნიკალური ID-ის გენერაცია
    if products:
        next_id = str(max(int(p['id']) for p in products) + 1)
    else:
        next_id = "1"
        
    new_product = {"id": next_id, "name": name, "price": price, "stock": stock}
    products.append(new_product)
    write_products(products)
    
    log_action(user, "ADD_PRODUCT", f"NAME={name}")
    print(f"\n✅ Product added successfully with ID: {next_id}")

# 4. პროდუქტის წაშლა
def delete_product(user):
    prod_id = input("Enter product ID to delete: ").strip()
    products = read_products()
    
    updated_products = [p for p in products if p['id'] != prod_id]
    
    if len(products) == len(updated_products):
        log_action(user, "DELETE_PRODUCT", f"PRODUCT_ID={prod_id} (FAILED - NOT FOUND)")
        print("\n❌ Product not found.")
    else:
        write_products(updated_products)
        log_action(user, "DELETE_PRODUCT", f"PRODUCT_ID={prod_id}")
        print("\n✅ Product deleted successfully.")

# მთავარი მენიუ
def main():
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