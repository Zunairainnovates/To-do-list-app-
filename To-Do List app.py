import tkinter as tk
from tkinter import messagebox

# -------- Main Window -------- #
root = tk.Tk()
root.title("Smart To-Do List")
root.geometry("450x550")
root.config(bg="#f0f4f7")

# -------- Functions -------- #

def add_task(event=None):
    task = entry.get().strip()
    if task:
        listbox.insert(tk.END, "☐ " + task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task!")

def delete_task():
    try:
        selected = listbox.curselection()[0]
        listbox.delete(selected)
    except:
        messagebox.showwarning("Selection Error", "Please select a task!")

def clear_tasks():
    if messagebox.askyesno("Confirm", "Are you sure you want to delete ALL tasks?"):
        listbox.delete(0, tk.END)

def mark_complete():
    try:
        selected = listbox.curselection()[0]
        task = listbox.get(selected)

        if task.startswith("☐"):
            listbox.delete(selected)
            listbox.insert(selected, "✔ " + task[2:])
        else:
            listbox.delete(selected)
            listbox.insert(selected, "☐ " + task[2:])
    except:
        messagebox.showwarning("Selection Error", "Select a task to mark!")

# -------- UI Components -------- #

title = tk.Label(root, text="My Smart To-Do List", 
                 font=("Arial", 20, "bold"), 
                 bg="#f0f4f7", fg="#2c3e50")
title.pack(pady=15)

entry = tk.Entry(root, font=("Arial", 14), width=30)
entry.pack(pady=10)
entry.bind("<Return>", add_task)  # Press Enter to add task

add_btn = tk.Button(root, text="Add Task", width=20,
                    bg="#27ae60", fg="white",
                    command=add_task)
add_btn.pack(pady=5)

# Frame for Listbox + Scrollbar
frame = tk.Frame(root)
frame.pack(pady=20)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox = tk.Listbox(frame, width=40, height=15,
                     font=("Arial", 12),
                     yscrollcommand=scrollbar.set)
listbox.pack()

scrollbar.config(command=listbox.yview)

complete_btn = tk.Button(root, text="Mark Complete / Undo",
                         width=25, bg="#2980b9",
                         fg="white", command=mark_complete)
complete_btn.pack(pady=5)

delete_btn = tk.Button(root, text="Delete Selected",
                       width=25, bg="#e74c3c",
                       fg="white", command=delete_task)
delete_btn.pack(pady=5)

clear_btn = tk.Button(root, text="Clear All Tasks",
                      width=25, bg="#8e44ad",
                      fg="white", command=clear_tasks)
clear_btn.pack(pady=5)

root.mainloop()