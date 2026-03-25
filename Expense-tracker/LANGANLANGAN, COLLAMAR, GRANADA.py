import tkinter as tk
from tkinter import messagebox

# Store expenses
expenses = []

# ---------- FUNCTIONS ----------

def add_expense():
    try:
        name = name_entry.get()
        category = category_entry.get()
        price = float(price_entry.get())

        if name == "" or category == "":
            messagebox.showerror("Error", "Please fill in all fields")
            return

        if price < 0:
            messagebox.showerror("Error", "Price cannot be negative")
            return

        expense = {
            "name": name,
            "category": category,
            "price": price
        }

        expenses.append(expense)

        history_list.insert(tk.END, f"{name} ({category}) - ₱{price}")

        name_entry.delete(0, tk.END)
        category_entry.delete(0, tk.END)
        price_entry.delete(0, tk.END)

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for price")


def show_summary():
    try:
        balance = float(balance_entry.get())
        goal = float(goal_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Enter valid numbers for balance and goal")
        return

    total_spent = sum(expense["price"] for expense in expenses)
    remaining = balance - total_spent

    summary = "\nExpense Summary\n\n"

    if not expenses:
        summary += "No expenses recorded.\n"
    else:
        for i, expense in enumerate(expenses, start=1):
            summary += f"{i}. {expense['name']} ({expense['category']}) - ₱{expense['price']}\n"

    summary += "\n----------------------"
    summary += f"\nTotal Spent: ₱{total_spent}"
    summary += f"\nRemaining Balance: ₱{remaining}"
    summary += "\n----------------------"

    if goal > 0:
        summary += f"\nSavings Goal: ₱{goal}"
        if remaining >= goal:
            summary += "\nYou reached your savings goal!"
        else:
            summary += "\nYou have not reached your savings goal yet."

    if remaining < 0:
        summary += "\nWARNING: You exceeded your balance!"
    elif remaining <= 100:
        summary += "\nBalance is very low."
    else:
        summary += "\nSpending is manageable."

    messagebox.showinfo("Summary", summary)


def clear_history():
    history_list.delete(0, tk.END)
    expenses.clear()


# ---------- WINDOW ----------

root = tk.Tk()
root.title("Expense Tracker")
root.geometry("480x600")
root.configure(bg="#0f172a")

# ---------- TITLE ----------

title = tk.Label(
    root,
    text="Expense Tracker",
    font=("Segoe UI", 22, "bold"),
    bg="#0f172a",
    fg="white"
)
title.pack(pady=15)

# ---------- BALANCE INPUT ----------

tk.Label(root, text="Bank Balance", bg="#0f172a", fg="white").pack()
balance_entry = tk.Entry(root, font=("Segoe UI", 11))
balance_entry.pack(pady=5)

tk.Label(root, text="Savings Goal", bg="#0f172a", fg="white").pack()
goal_entry = tk.Entry(root, font=("Segoe UI", 11))
goal_entry.pack(pady=5)

# ---------- EXPENSE INPUT ----------

tk.Label(root, text="Expense Name", bg="#0f172a", fg="white").pack(pady=5)
name_entry = tk.Entry(root, font=("Segoe UI", 11))
name_entry.pack()

tk.Label(root, text="Category", bg="#0f172a", fg="white").pack(pady=5)
category_entry = tk.Entry(root, font=("Segoe UI", 11))
category_entry.pack()

tk.Label(root, text="Price", bg="#0f172a", fg="white").pack(pady=5)
price_entry = tk.Entry(root, font=("Segoe UI", 11))
price_entry.pack()

# ---------- BUTTONS ----------

add_btn = tk.Button(
    root,
    text="Add Expense",
    command=add_expense,
    bg="#22c55e",
    fg="white",
    font=("Segoe UI", 11),
    width=20
)
add_btn.pack(pady=10)

summary_btn = tk.Button(
    root,
    text="View Summary",
    command=show_summary,
    bg="#3b82f6",
    fg="white",
    font=("Segoe UI", 11),
    width=20
)
summary_btn.pack(pady=5)

clear_btn = tk.Button(
    root,
    text="Clear History",
    command=clear_history,
    bg="#ef4444",
    fg="white",
    font=("Segoe UI", 11),
    width=20
)
clear_btn.pack(pady=5)

# ---------- HISTORY SECTION ----------

history_title = tk.Label(
    root,
    text="Expense History",
    font=("Segoe UI", 13, "bold"),
    bg="#0f172a",
    fg="white"
)
history_title.pack(pady=10)

history_list = tk.Listbox(root, width=50, height=12)
history_list.pack()

# ---------- RUN PROGRAM ----------

root.mainloop()
