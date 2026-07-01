import tkinter as tk
from tkinter import ttk, messagebox
from core import InventoryItem

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
    tk.Label(header_frame, text="Name", bg=card_dark, font=("Segoe UI", 9, "bold"), fg=text_light).grid(row=0, column=0, sticky="w", padx=5)
    name_entry = tk.Entry(header_frame, font=("Segoe UI", 11), width=15, bg="#3b3b4d", fg="white", insertbackground="white", relief="flat")
    name_entry.grid(row=1, column=0, padx=5, pady=5)

    tk.Label(header_frame, text="Description", bg=card_dark, font=("Segoe UI", 9, "bold"), fg=text_light).grid(row=0, column=1, sticky="w", padx=5)
    desc_entry = tk.Entry(header_frame, font=("Segoe UI", 11), width=25, bg="#3b3b4d", fg="white", insertbackground="white", relief="flat")
    desc_entry.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(header_frame, text="Category", bg=card_dark, font=("Segoe UI", 9, "bold"), fg=text_light).grid(row=0, column=2, sticky="w", padx=5)
    cat_entry = tk.Entry(header_frame, font=("Segoe UI", 11), width=15, bg="#3b3b4d", fg="white", insertbackground="white", relief="flat")
    cat_entry.grid(row=1, column=2, padx=5, pady=5)

    tk.Label(header_frame, text="Quantity", bg=card_dark, font=("Segoe UI", 9, "bold"), fg=text_light).grid(row=0, column=3, sticky="w", padx=5)
    qty_entry = tk.Entry(header_frame, font=("Segoe UI", 11), width=10, bg="#3b3b4d", fg="white", insertbackground="white", relief="flat")
    qty_entry.grid(row=1, column=3, padx=5, pady=5)

    # --- Table ---
    table_frame = tk.Frame(container, bg=bg_dark)
    table_frame.pack(fill="both", expand=True, padx=10, pady=5)

    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Inv.Treeview", background=card_dark, foreground=text_light, fieldbackground=card_dark, rowheight=35, borderwidth=0)
    style.configure("Inv.Treeview.Heading", background=border_color, foreground=text_light, relief="flat", font=("Segoe UI", 10, "bold"))
    style.map("Inv.Treeview", background=[('selected', accent_green)])

    tree = ttk.Treeview(table_frame, columns=("ID", "Name", "Desc", "Cat", "Qty"), show="headings", style="Inv.Treeview")

    headers = [("ID", 50), ("Name", 200), ("Desc", 350), ("Cat", 150), ("Qty", 100)]
    for col, width in headers:
        tree.heading(col, text=col.upper(), anchor="center")
        tree.column(col, width=width, anchor="center")

    tree.pack(fill="both", expand=True)

    def add_item():
        try:
            name, desc = name_entry.get().strip(), desc_entry.get().strip()
            cat, qty = cat_entry.get().strip(), qty_entry.get().strip()

            if not name or not desc or not cat or not qty:
                messagebox.showwarning("Input Error", "All fields must be filled out!")
                return

            new_item = InventoryItem(name, desc, cat, qty)

            from data import save_inventory_item
            manager.add_inventory_item(new_item)
            save_inventory_item(new_item)

            tree.insert("", "end", values=[new_item.id, new_item.name, new_item.description, new_item.category, new_item.quantity])

            for e in [name_entry, desc_entry, cat_entry, qty_entry]:
                e.delete(0, tk.END)
            name_entry.focus()

        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def delete_item():
        selected = tree.selection()
        if not selected:
            messagebox.showwarning("Selection Error", "Please select an item to delete.")
            return

        if not messagebox.askyesno("Confirm", "Delete selected item?"): return

        for item in selected:
            vals = tree.item(item, "values")
            target_id = int(vals[0])

            manager.inventory = [i for i in manager.inventory if i.id != target_id]
            tree.delete(item)

        from data import rewrite_all_inventory
        rewrite_all_inventory(manager.inventory)

    tk.Button(header_frame, text="Add Item", bg=accent_green, fg="white", font=("Segoe UI", 10, "bold"),
              padx=15, command=add_item, relief="flat", cursor="hand2").grid(row=1, column=4, padx=10)

    tk.Button(header_frame, text="Delete Selected", bg=accent_red, fg="white", font=("Segoe UI", 10, "bold"),
              padx=15, command=delete_item, relief="flat", cursor="hand2").grid(row=1, column=5, padx=5)

    for item in manager.inventory:
        tree.insert("", "end", values=[item.id, item.name, item.description, item.category, item.quantity])
