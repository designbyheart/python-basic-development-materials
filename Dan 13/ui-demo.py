import tkinter as tk

root = tk.Tk()
root.geometry("300x200")

label = tk.Label(root, text="Username:")
entry = tk.Entry(root)
# submit_button = tk.Button(root, text="Submit")

# Place widgets at specific coordinates
label.place(x=50, y=50)
entry.place(x=120, y=50)

def on_button_click():
    print("Button was clicked!")

button = tk.Button(root, text="Click Me", command=on_button_click)
button.pack()

def validate_input():
    user_input = entry.get()
    if len(user_input) == 0:
        print("Input cannot be empty!")
    else:
        print(f"Input accepted: {user_input}")

submit_button = tk.Button(root, text="Submit", command=validate_input)
submit_button.pack()
submit_button.place(x=100, y=100)

root.mainloop()

