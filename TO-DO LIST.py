#ROSHAN IMMANUEL E
from tkinter import *
from tkinter import messagebox

a = Tk()
a.title("To-DO list")
a.geometry("800x600")

# Frame for adding tasks
frame_add = Frame(a)
frame_add.pack(pady=10)

l1 = Label(frame_add, text="Enter your tasks/To-Do")
l1.pack(pady=5)

entry1 = Entry(frame_add, width=50)
entry1.pack(pady=5)

def add():
    try:
        EN1 = entry1.get().strip()
        if EN1:
            list_var.insert(END, EN1)
            entry1.delete(0, END)
        else:
            messagebox.showerror("ERROR", "Enter something")
    except Exception as ex:
        messagebox.showerror("ERROR", str(ex))

b1 = Button(frame_add, text="Add", command=add)
b1.pack(pady=5)

# setting up the Frame for updating task
frame_update = Frame(a)
frame_update.pack(pady=10)

Label(frame_update, text="Enter new text for update:").pack(pady=5)

entry2 = Entry(frame_update, width=50)
entry2.pack(pady=5)

def update():
    try:
        selected=list_var.curselection()[0]
        new_text=entry2.get().strip()
        if new_text:
            list_var.delete(selected)
            list_var.insert(selected, new_text)
            entry2.delete(0, END)
        else:
            messagebox.showerror("ERROR", "Enter new text to update")
    except Exception as ex:
        messagebox.showerror("ERROR", "Select a task to update")

update_button = Button(frame_update, text="Update", command=update)
update_button.pack(pady=5)

# building widgets for delete and tracking
def delete():
    try:
        selected = list_var.curselection()
        list_var.delete(selected[0])
    except Exception as ex:
        messagebox.showerror("ERROR", "Enter a valid selection")

b2 = Button(a, text="Delete", command=delete)
b2.pack(pady=5)

def mark_complete():
    try:
        selected = list_var.curselection()[0]
        task = list_var.get(selected)
        if not task.startswith("[Done] "):
            list_var.delete(selected)
            list_var.insert(selected, "[Done] " + task)
        else:
            messagebox.showinfo("INFO", "Task already marked as complete")
    except Exception as ex:
        messagebox.showerror("ERROR", "Select a task to mark complete")

track_button = Button(a, text="Mark Complete", command=mark_complete)
track_button.pack(pady=5)

#Label and list box for displaying tasks
l2 = Label(a, text="YOUR TASK/TO-DO LIST")
l2.pack(pady=5)

list_var = Listbox(a, width=50, height=10)
list_var.pack(pady=10)

a.mainloop()
