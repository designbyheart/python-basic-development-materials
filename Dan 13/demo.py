import tkinter as tk

def on_button_click():
    print("Button clicked!")

# Create the main application window
root = tk.Tk()
root.title("My First GUI App")
root.geometry("400x300")

# Add a button widget
button = tk.Button(root, text="Click Me!", command=on_button_click)
button.pack(pady=20)  # Add some padding for aesthetics

# Start the application
root.mainloop()