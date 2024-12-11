import tkinter as tk

root = tk.Tk() 
class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")

        self.task_entry = tk.Entry(root)
        self.task_entry.pack()

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack()

        self.task_listbox = tk.Listbox(root)
        self.task_listbox.pack()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)

# Run the application
app = ToDoApp(root)
root.mainloop()