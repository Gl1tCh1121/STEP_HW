import tkinter as tk
from models import BusinessManager, format_currency
import sale
import expense
import inventory
import edit

class Manager:
    def __init__(self, root):
        self.root = root
        self.root.title("Manager Business Suite")
        self.root.geometry("1100x700")

        self.bg_dark, self.card_dark = "#1e1e26", "#2d2d3a"
        self.text_light, self.accent_blue = "#e0e0e0", "#3d85c6"
        self.nav_color = "#15151c"

        self.root.configure(bg=self.bg_dark)
        self.manager = BusinessManager()

        # 1. TOP NAVIGATION MENU
        self.nav_frame = tk.Frame(self.root, bg=self.nav_color, height=50)
        self.nav_frame.pack(fill="x", side="top")

        nav_buttons = [
            ("Sales", self.show_sales),
            ("Expenses", self.show_expenses),
            ("Inventory", self.show_inventory),
            ("Editor", self.show_editor)
        ]

        for text, command in nav_buttons:
            btn = tk.Button(self.nav_frame, text=text, bg=self.nav_color, fg=self.text_light,
                            font=("Segoe UI", 10, "bold"), relief="flat", padx=20,
                            activebackground=self.accent_blue, cursor="hand2", command=command)
            btn.pack(side="left", pady=10)

        # 2. FOOTER (For Totals)
        self.footer_frame = tk.Frame(self.root, bg=self.nav_color, height=40)
        self.footer_frame.pack(fill="x", side="bottom")
        self.total_label = tk.Label(self.footer_frame, text="", bg=self.nav_color, fg=self.text_light, font=("Segoe UI", 11, "bold"))
        self.total_label.pack(pady=5)

        # 3. MAIN CONTENT AREA
        self.content_area = tk.Frame(self.root, bg=self.bg_dark)
        self.content_area.pack(fill="both", expand=True)

        self.load_startup_data()

    def load_startup_data(self):
        self.manager.transactions = []
        self.manager.inventory = []

        from data import load_all_transactions, load_all_expenses, load_all_inventory

        for tx in load_all_transactions():
            self.manager.add_transaction(tx)

        for tx in load_all_expenses():
            self.manager.add_transaction(tx)

        for item in load_all_inventory():
            self.manager.add_inventory_item(item)

        self.update_dashboard_totals()
        self.show_sales()

    def clear_content(self):
        for widget in self.content_area.winfo_children():
            widget.destroy()

    def show_sales(self):
        self.clear_content()
        sale.load_view(self.content_area, self.manager, self.update_dashboard_totals)

    def show_expenses(self):
        self.clear_content()
        expense.load_view(self.content_area, self.manager, self.update_dashboard_totals)

    def show_inventory(self):
        self.clear_content()
        inventory.load_view(self.content_area, self.manager, self.update_dashboard_totals)

    def show_editor(self):
        self.clear_content()
        edit.load_view(self.content_area, self.manager, self.update_dashboard_totals)

    def update_dashboard_totals(self):
        totals = self.manager.get_totals()
        status_text = (f"Sales: {format_currency(totals['sales'])}  |  "
                       f"Expenses: {format_currency(totals['expenses'])}  |  "
                       f"Net: {format_currency(totals['net'])}")
        self.total_label.config(text=status_text)

def main():
    root = tk.Tk()
    Manager(root)
    root.mainloop()

if __name__ == "__main__":
    main()
