from tkinter import *

expenses = []
budget = 5000

def add_expense():
    try:
        name = name_entry.get()
        amount = float(amount_entry.get())

        expenses.append((name, amount))

        expense_list.insert(
            END,
            f"{name} - ₹{amount}"
        )

        update_summary()

        name_entry.delete(0, END)
        amount_entry.delete(0, END)

    except ValueError:
        total_label.config(text="Enter a valid amount!")

def update_summary():
    total = sum(amount for name, amount in expenses)
    remaining = budget - total

    total_label.config(
        text=f"Total Spent: ₹{total}"
    )

    remaining_label.config(
        text=f"Remaining: ₹{remaining}"
    )


root = Tk()
root.title(" Expense Tracker")
root.geometry("500x500")

title = Label(
    root,
    text=" Expense Tracker",
    font=("Arial", 20, "bold")
)
title.pack(pady=10)

Label(root, text="Expense Name").pack()

name_entry = Entry(root, width=30)
name_entry.pack()

Label(root, text="Amount").pack()

amount_entry = Entry(root, width=30)
amount_entry.pack()

Button(
    root,
    text="Add Expense",
    command=add_expense,
    bg="blue",
    fg="white"
).pack(pady=10)

expense_list = Listbox(root, width=50)
expense_list.pack(pady=10)

Label(
    root,
    text=f"Budget: ₹{budget}",
    font=("Arial", 12)
).pack()

total_label = Label(
    root,
    text="Total Spent: ₹0",
    font=("Arial", 12)
)
total_label.pack()

remaining_label = Label(
    root,
    text=f"Remaining: ₹{budget}",
    font=("Arial", 12)
)
remaining_label.pack()

root.mainloop()