import tkinter as tk
from tkinter import messagebox

# ------------------ LINKED LIST IMPLEMENTATION ------------------

class Node:
    def __init__(self, item, qty, price):
        self.item = item
        self.qty = qty
        self.price = price
        self.next = None



class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, item, qty, price):
        new_node = Node(item, qty, price)

        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    def traverse(self):
        temp = self.head
        data = []
        while temp:
            data.append(temp)
            temp = temp.next
        return data

    def calculate_total(self):
        temp = self.head
        total = 0
        while temp:
            total += temp.price
            temp = temp.next
        return total

    def clear(self):
        self.head = None


# ------------------ GROCERY ITEMS ------------------

items = {
    "Rice": 120,
    "Sugar": 80,
    "Milk": 60,
    "Oil": 200,
    "Bread": 70,
    "Eggs": 12
}

bill_list = LinkedList()


# ------------------ FUNCTIONS ------------------

def add_item():
    item = item_var.get()
    qty = qty_entry.get()

    if item == "" or qty == "":
        messagebox.showerror("Error", "Select item and enter quantity")
        return

    qty = int(qty)
    price = items[item] * qty

    bill_list.insert(item, qty, price)

    bill_area.insert(tk.END, f"{item}\t{qty}\tRs.{price}\n")
    qty_entry.delete(0, tk.END)


def total_bill():
    total = bill_list.calculate_total()
    total_label.config(text=f"Total Bill: Rs. {total}")


def clear_bill():
    bill_list.clear()
    bill_area.delete("1.0", tk.END)
    bill_area.insert(tk.END, "Item\tQty\tPrice\n")
    bill_area.insert(tk.END, "---------------------------\n")
    total_label.config(text="Total Bill: Rs. 0")


# ------------------ GUI ------------------

root = tk.Tk()
root.title("Grocery Billing System (DSA Project)")
root.geometry("450x500")

tk.Label(root, text="Grocery Billing System", font=("Arial", 16, "bold")).pack(pady=10)

frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="Item:").grid(row=0, column=0)
item_var = tk.StringVar()
tk.OptionMenu(frame, item_var, *items.keys()).grid(row=0, column=1)

tk.Label(frame, text="Quantity:").grid(row=1, column=0)
qty_entry = tk.Entry(frame)
qty_entry.grid(row=1, column=1)

btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Add Item", command=add_item).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Total", command=total_bill).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Clear", command=clear_bill).grid(row=0, column=2, padx=5)

bill_area = tk.Text(root, height=12, width=40)
bill_area.pack(pady=10)
bill_area.insert(tk.END, "Item\tQty\tPrice\n")
bill_area.insert(tk.END, "---------------------------\n")

total_label = tk.Label(root, text="Total Bill: Rs. 0", font=("Arial", 12, "bold"))
total_label.pack(pady=10)

root.mainloop()
