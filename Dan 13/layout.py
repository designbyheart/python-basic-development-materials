import tkinter as tk

root = tk.Tk()
root.geometry("300x200")

label = tk.Label(root, text="Username:")
entry = tk.Entry(root)
submit_button = tk.Button(root, text="Submit")

# Place widgets at specific coordinates
label.place(x=50, y=50)
entry.place(x=70, y=60)
submit_button.place(x=100, y=100)

root.mainloop()