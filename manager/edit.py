import tkinter as tk
from tkinter import ttk, messagebox
from core import Transaction, Expense, InventoryItem

def load_view(parent, manager, update_totals_callback):
    bg_dark, card_dark = "#1e1e26", "#2d2d3a"
    text_light, accent_blue = "#e0e0e0", "#3d85c6"
    border_color = "#3f3f4f"

    container = tk.Frame(parent, bg=bg_dark)
    container.pack(fill="both", expand=True)

    # --- TOP CONTROL FRAME ---
    ctrl_frame = tk.Frame(container, bg=card_dark, padx=10, pady=10, highlightthickness=1, highlightbackground=border_color)
    ctrl_frame.pack(fill="x", padx=10, pady=5)

    tk.Label(ctrl_frame, text="Select Dataset:", bg=card_dark, fg=text_light, font=("Segoe UI", 10, "bold")).pack(side="left", padx=5)

    dataset_var = tk.StringVar(value="Sales")
    selector = ttk.Combobox(ctrl_frame, textvariable=dataset_var, values=["Sales", "Expenses", "Inventory"], state="readonly", width=15)
    selector.pack(side="left", padx=5)

    # --- INPUT/EDIT FIELDS FRAME ---
    edit_frame = tk.Frame(container, bg=card_dark, padx=10, pady=15, highlightthickness=1, highlightbackground=border_color)
    edit_frame.pack(fill="x", padx=10, pady=5)

    entries = {}
    labels = ["Field 1", "Field 2", "Field 3", "Field 4"]

    for i, label_text in enumerate(labels):
        lbl = tk.Label(edit_frame, text=label_text, bg=card_dark, fg=text_light, font=("Segoe UI", 9, "bold"))
        lbl.grid(row=0, column=i, sticky="w", padx=10)
        ent = tk.Entry(edit_frame, font=("Segoe UI", 11), bg="#3b3b4d", fg="white", relief="flat", insertbackground="white")
        ent.grid(row=1, column=i, padx=10, pady=5)
        entries[labels[i]] = (lbl, ent)

    # --- TABLE AREA ---
    table_frame = tk.Frame(container, bg=bg_dark)
    table_frame.pack(fill="both", expand=True, padx=10, pady=10)

    tree = ttk.Treeview(table_frame, show="headings", selectmode="browse")
    tree.pack(fill="both", expand=True)

    # --- FUNCTIONS ---

    def refresh_table(*args):
        mode = dataset_var.get()
        tree.delete(*tree.get_children())

        if mode == "Sales":
            cols = ("ID", "Date", "Customer", "Product", "Amount")
            field_names = ["Customer", "Product", "Description", "Amount"]
        elif mode == "Expenses":
            cols = ("ID", "Date", "Name", "Description", "Amount")
            field_names = ["Name", "Description", "Amount", ""]
        else:
            cols = ("ID", "Name", "Description", "Category", "Qty")
            field_names = ["Name", "Description", "Category", "Quantity"]

        tree["columns"] = cols
        for c in cols:
            tree.heading(c, text=c.upper(), anchor="center")
            tree.column(c, width=70 if c == "ID" else 180, anchor="center")

        for i, name in enumerate(field_names):
            label_widget, entry_widget = entries[labels[i]]
            if name == "":
                label_widget.grid_remove()
                entry_widget.grid_remove()
            else:
                label_widget.grid()
                label_widget.config(text=name)
                entry_widget.grid()
                entry_widget.delete(0, tk.END)

        if mode == "Sales":
            data = [t for t in manager.transactions if isinstance(t, Transaction)]
            for t in data: tree.insert("", "end", values=[t.id, t.date, t.customer, t.product, f"${t.amount:,.2f}"])
        elif mode == "Expenses":
            data = [t for t in manager.transactions if isinstance(t, Expense)]
            for t in data: tree.insert("", "end", values=[t.id, t.date, t.name, t.description, f"${t.amount:,.2f}"])
        else:
            for i in manager.inventory: tree.insert("", "end", values=[i.id, i.name, i.description, i.category, i.quantity])

    def on_row_select(event):
        selected = tree.selection()
        if not selected: return

        vals = tree.item(selected[0], "values")
        mode = dataset_var.get()
        target_id = int(vals[0])

        for l in labels: entries[l][1].delete(0, tk.END)

        if mode == "Sales":
            obj = next(t for t in manager.transactions if t.id == target_id and isinstance(t, Transaction))
            data = [obj.customer, obj.product, obj.description, obj.amount]
        elif mode == "Expenses":
            obj = next(t for t in manager.transactions if t.id == target_id and isinstance(t, Expense))
            data = [obj.name, obj.description, obj.amount]
        else:
            obj = next(i for i in manager.inventory if i.id == target_id)
            data = [obj.name, obj.description, obj.category, obj.quantity]

        for i, val in enumerate(data):
            entries[labels[i]][1].insert(0, str(val))

    def save_edit():
        selected = tree.selection()
        if not selected:
            messagebox.showwarning("Edit Error", "Select a row to edit first!")
            return

        target_id = int(tree.item(selected[0], "values")[0])
        mode = dataset_var.get()

        val_list = [entries[l][1].get().strip() for l in labels]

        try:
            from data import rewrite_all_data, rewrite_all_inventory

            if mode == "Sales":
                obj = next(t for t in manager.transactions if t.id == target_id and isinstance(t, Transaction))
                obj.customer, obj.product, obj.description, obj.amount = val_list[0], val_list[1], val_list[2], float(val_list[3])
                rewrite_all_data(manager.transactions)
            elif mode == "Expenses":
                obj = next(t for t in manager.transactions if t.id == target_id and isinstance(t, Expense))
                obj.name, obj.description, obj.amount = val_list[0], val_list[1], float(val_list[2])
                rewrite_all_data(manager.transactions)
            else:
                obj = next(i for i in manager.inventory if i.id == target_id)
                obj.name, obj.description, obj.category, obj.quantity = val_list[0], val_list[1], val_list[2], int(val_list[3])
                rewrite_all_inventory(manager.inventory)

            messagebox.showinfo("Success", "Record updated successfully!")
            refresh_table()
            update_totals_callback()
        except ValueError:
            messagebox.showerror("Error", "Check your Number/Quantity format!")
        except Exception as e:
            messagebox.showerror("Error", f"Update failed: {e}")

    selector.bind("<<ComboboxSelected>>", refresh_table)
    tree.bind("<<TreeviewSelect>>", on_row_select)

    tk.Button(ctrl_frame, text="Update Record", bg=accent_blue, fg="white", font=("Segoe UI", 10, "bold"),
              padx=20, command=save_edit, relief="flat", cursor="hand2").pack(side="right", padx=10)

    tk.Button(ctrl_frame, text="Clear Fields", bg="#444", fg="white", font=("Segoe UI", 10, "bold"),
              padx=15, command=lambda: [entries[l][1].delete(0, tk.END) for l in labels],
              relief="flat", cursor="hand2").pack(side="right")

    refresh_table()
