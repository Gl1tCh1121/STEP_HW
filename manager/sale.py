import tkinter as tk
from tkinter import ttk, messagebox
from core import Transaction

#LOADING WINDOW

def load_view(parent, manager, update_totals_callback):

    bg_dark, card_dark = "#1e1e26", "#2d2d3a"
    text_light, accent_green, accent_red = "#e0e0e0", "#28a745", "#f87171"
    border_color = "#3f3f4f"

    container = tk.Frame(parent, bg=bg_dark)
    container.pack(fill="both", expand=True)

    header_frame = tk.Frame(container, bg=card_dark, padx=10, pady=15,
                            highlightthickness=1, highlightbackground=border_color)
    header_frame.pack(fill="x", padx=10, pady=(0, 10))

    # --- Inputs ---

    tk.Label(header_frame, text="Customer", bg=card_dark, font=("Segoe UI", 9, "bold"), fg=text_light).grid(row=0, column=0, sticky="w", padx=5)
    cust_entry = tk.Entry(header_frame, font=("Segoe UI", 11), width=15, bg="#3b3b4d", fg="white", insertbackground="white", relief="flat")
    cust_entry.grid(row=1, column=0, padx=5, pady=5)

    tk.Label(header_frame, text="Product", bg=card_dark, font=("Segoe UI", 9, "bold"), fg=text_light).grid(row=0, column=1, sticky="w", padx=5)
    prod_entry = tk.Entry(header_frame, font=("Segoe UI", 11), width=15, bg="#3b3b4d", fg="white", insertbackground="white", relief="flat")
    prod_entry.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(header_frame, text="Description", bg=card_dark, font=("Segoe UI", 9, "bold"), fg=text_light).grid(row=0, column=2, sticky="w", padx=5)
    desc_entry = tk.Entry(header_frame, font=("Segoe UI", 11), width=20, bg="#3b3b4d", fg="white", insertbackground="white", relief="flat")
    desc_entry.grid(row=1, column=2, padx=5, pady=5)

    tk.Label(header_frame, text="Amount ($)", bg=card_dark, font=("Segoe UI", 9, "bold"), fg=text_light).grid(row=0, column=3, sticky="w", padx=5)
    amt_entry = tk.Entry(header_frame, font=("Segoe UI", 11), width=10, bg="#3b3b4d", fg="white", insertbackground="white", relief="flat")
    amt_entry.grid(row=1, column=3, padx=5, pady=5)

    # --- Table ---

    table_frame = tk.Frame(container, bg=bg_dark)
    table_frame.pack(fill="both", expand=True, padx=10, pady=5)

    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Treeview", background=card_dark, foreground=text_light, fieldbackground=card_dark, rowheight=35, borderwidth=0)
    style.configure("Treeview.Heading", background=border_color, foreground=text_light, relief="flat", font=("Segoe UI", 10, "bold"))
    style.map("Treeview", background=[('selected', accent_green)])

    tree = ttk.Treeview(table_frame, columns=("ID", "Date", "Cust", "Prod", "Desc", "Amt"), show="headings")

    headers = [("ID", 50), ("Date", 100), ("Cust", 150), ("Prod", 150), ("Desc", 300), ("Amt", 120)]
    for col, width in headers:
        tree.heading(col, text=col.upper(), anchor="center")
        tree.column(col, width=width, anchor="center")

    tree.pack(fill="both", expand=True)

    def add_sale():
        try:
            customer = cust_entry.get().strip()
            product = prod_entry.get().strip()
            description = desc_entry.get().strip()
            amount = amt_entry.get().strip()

            if not customer or not product or not description or not amount:
                messagebox.showwarning("Input Error", "All fields must be filled out!")
                return

            new_tx = Transaction(customer, product, description, "Sale", amount)

            from data import save_transaction
            manager.add_transaction(new_tx)
            save_transaction(new_tx)

            tree.insert("", 0, values=[new_tx.id, new_tx.date, new_tx.customer, new_tx.product, new_tx.description, f"${new_tx.amount:,.2f}"])

            for e in [cust_entry, prod_entry, desc_entry, amt_entry]:
                e.delete(0, tk.END)
            cust_entry.focus()
            update_totals_callback()

        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def delete_sale():
        selected_item = tree.selection()
        if not selected_item:
            messagebox.showwarning("Selection Error", "Please select a sale to delete.")
            return

        if not messagebox.askyesno("Confirm", "Delete selected sale?"):
            return

        for item in selected_item:
            vals = tree.item(item, "values")
            target_id = int(vals[0])

            manager.transactions = [tx for tx in manager.transactions if tx.id != target_id]

            tree.delete(item)

        from data import rewrite_all_data
        rewrite_all_data(manager.transactions)
        update_totals_callback()

    tk.Button(header_frame, text="Record Sale", bg=accent_green, fg="white", font=("Segoe UI", 10, "bold"),
              padx=15, command=add_sale, relief="flat", cursor="hand2").grid(row=1, column=4, padx=10)

    tk.Button(header_frame, text="Delete Selected", bg=accent_red, fg="white", font=("Segoe UI", 10, "bold"),
              padx=15, command=delete_sale, relief="flat", cursor="hand2").grid(row=1, column=5, padx=5)

    for tx in manager.transactions:
        if tx.category == "Sale":
            tree.insert("", "end", values=[tx.id,tx.date, tx.customer, tx.product, tx.description, f"${tx.amount:,.2f}"])
