import tkinter as tk
from tkinter import ttk
import csv
import os
import datetime

FILE_PATH = "โปรเจคจ้บ.csv"

class IncomeExpenseTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Income and Expense Tracker")

        # Set window size
        self.root.geometry("600x400")

        self.create_widgets()

    def create_widgets(self):
        # Create a style to customize the appearance
        style = ttk.Style(self.root)
        style.configure("TFrame", background="#f0f0f0")  # Set background color
        style.configure("TButton", background="#4caf50", foreground="black")  # Set button colors
        style.configure("TLabel", background="#f0f0f0", foreground="black")  # Set label background color
        style.configure("Treeview", foreground="black")  # Set Treeview text color

        # Create a frame with a style
        frame = ttk.Frame(self.root, style="TFrame")
        frame.place(relx=0.5, rely=0.5, anchor="center")

        # Labels and Entry widgets
        ttk.Label(frame, text="Amount:", style="TLabel").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.amount_entry = ttk.Entry(frame)
        self.amount_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        ttk.Label(frame, text="Category:", style="TLabel").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.category_var = tk.StringVar()
        category_options = ["Food expenses", "Travel expenses", "Shopping", "Entertainment", "Paying bills", "Others", "Income"]
        self.category_combobox = ttk.Combobox(frame, textvariable=self.category_var, values=category_options, state="readonly")
        self.category_combobox.grid(row=1, column=1, padx=5, pady=5, sticky="w")
        self.category_combobox.set(category_options[0])

        ttk.Label(frame, text="Description:", style="TLabel").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.description_entry = ttk.Entry(frame)
        self.description_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w")

        # Buttons with custom style
        ttk.Button(frame, text="Record Transaction", command=self.record_transaction).grid(row=3, column=0, columnspan=2, pady=10, sticky="we")
        ttk.Button(frame, text="View Transactions", command=self.view_transactions).grid(row=4, column=0, columnspan=2, pady=10, sticky="we")
        ttk.Button(frame, text="Exit", command=self.root.destroy).grid(row=5, column=0, columnspan=2, pady=10, sticky="we")

    def record_transaction(self):
        amount = self.amount_entry.get()
        category = self.category_var.get()
        description = self.description_entry.get()

        if not amount:
            return

        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(FILE_PATH, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([date, category, amount, description])

        self.amount_entry.delete(0, tk.END)
        self.description_entry.delete(0, tk.END)

    def view_transactions(self):
        transactions_window = tk.Toplevel(self.root)
        transactions_window.title("Transactions")

        tree = ttk.Treeview(transactions_window)
        tree["columns"] = ("Date", "Category", "Amount", "Description")
        tree.heading("#0", text="", anchor="w")
        tree.column("#0", anchor="w", width=1)

        headers = ["Date", "Category", "Amount", "Description"]
        for col, header in enumerate(headers):
            tree.heading(col, text=header, anchor="w")
            tree.column(col, anchor="w", width=120)

        try:
            with open(FILE_PATH, "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    tree.insert("", "end", values=row)
        except FileNotFoundError:
            tree.insert("", "end", values=["No transactions recorded yet."])

        tree.pack(expand=True, fill="both")

if __name__ == "__main__":
    root = tk.Tk()
    app = IncomeExpenseTracker(root)
    root.mainloop()
